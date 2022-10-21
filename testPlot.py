from cProfile import label
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y_values = []
y2_values = []

index = count()
fig, (graphX,graphY) = plt.subplots(nrows=2, ncols=1)
# fig2, graphY = plt.subplots()

def animate(i):
    data = pd.read_csv('data.csv')
    x_values = data['Time']
    y_values = data['GyroX']
    y2_values = data['GyroY']
    
    
    # Subplotting
   

   
    # plt.subplot(2,1,1)
    plt.cla()
    # graphX.legend()
    graphX.plot(x_values, y_values)
    graphY.plot(x_values, y2_values)
    
    
    
    graphX.set_xlabel('Time')
    graphX.set_ylabel('GyroX')
    graphX.set_title('Gyroscope X')
    # # if(len(y_values)> 50):
    # #     plt.xlim([y_values[y_values.idxmax()]-50, y_values[y_values.idxmax()]])
    
    # plt.subplot(2,1,2)
    # plt.cla()
    # graphY.legend()
    
    graphY.set_xlabel('Time')
    graphY.set_ylabel('GyroY')
    graphY.set_title('Gyroscope Y')
    
    # plt.gcf().autofmt_xdate()
    
    
    

ani = FuncAnimation(plt.gcf(), animate, interval=1500)

# plt.cla()
plt.tight_layout()
plt.show()