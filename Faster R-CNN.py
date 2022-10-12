import torch
import torchvision
from torchvision.models._utils import IntermediateLayerGetter
import numpy as np

from torchvision.transforms import transforms as transforms
import random
import cv2

from PIL import Image

coco_names = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.to(device)

print("FIN")

def get_outputs(image, model, threshold):
    with torch.no_grad():
        # forward pass of the image through the modle
        outputs = model(image)
    
    # get all the scores
    scores = list(outputs[0]['scores'].detach().cpu().numpy())
    # index of those scores which are above a certain threshold
    thresholded_preds_inidices = [scores.index(i) for i in scores if i > threshold]
    thresholded_preds_count = len(thresholded_preds_inidices)
    # get the bounding boxes, in (x1, y1), (x2, y2) format
    boxes = [[(int(i[0]), int(i[1])), (int(i[2]), int(i[3]))]  for i in outputs[0]['boxes'].detach().cpu()]
    # discard bounding boxes below threshold value
    boxes = boxes[:thresholded_preds_count]
    # get the classes labels
    labels = [coco_names[i] for i in outputs[0]['labels']]
    return boxes, labels

def draw_segmentation_map(image, boxes, labels):
    for i in range(len(boxes)):
        # apply a randon color mask to each object
        color = COLORS[random.randrange(0, len(COLORS))]
        #convert the original PIL image into NumPy format
        image = np.array(image)
        # convert from RGN to OpenCV BGR format
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # draw the bounding boxes around the objects
        cv2.rectangle(image, boxes[i][0], boxes[i][1], color=color, thickness=2)
        # put the label text above the objects
        cv2.putText(image , labels[i], (boxes[i][0][0], boxes[i][0][1]-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 
                    thickness=2, lineType=cv2.LINE_AA)
    
    return image

def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img = mpimg.imread(result)
#imgplot = plt.imshow(img)
#plt.show()

path = 'Frame/frame1001.jpg'
img_pil = Image.open(path).convert('RGB')
tensor = torchvision.transforms.functional.to_tensor(img_pil)
list_img = [tensor.to(device)]
model.eval()

#with torch.no_grad():
predictions = model(list_img)

predictions[0].keys()
transform = transforms.Compose([transforms.ToTensor()])
COLORS = np.random.uniform(0, 255, size=(len(coco_names), 3))
image = Image.open(path).convert('RGB')
# keep a copy of the original image for OpenCV functions and applying masks
orig_image = image.copy()
# transform the image
image = transform(image)
# add a batch dimension
image = image.unsqueeze(0).to(device)
boxes, labels = get_outputs(image, model, 0.7)
result = draw_segmentation_map(orig_image, boxes, labels)
cv2.imshow('graycsale image',result)
cv2.waitKey(0)
outputs = []
hook = model.backbone.register_forward_hook(lambda self, list_img, output: outputs.append(output))
res = model(list_img)
hook.remove()
selected_rois = model.roi_heads.box_roi_pool(outputs[0], [r['boxes'] for r in res], [i.shape[-2:] for i in list_img])
print(selected_rois.shape)
activation = {}
model.roi_heads.box_head.fc6.register_forward_hook(get_activation('fc6'))