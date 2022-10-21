import csv
import random
import time

timeLapse = 0
sensorValueX = 3.2
sensorValueY = 3.4


fieldnames = ["Time", "GyroX", "GyroY"]
maxDataToShow = 50
counter = 0

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
        
    with open('data.csv', 'a') as csv_file:
        # if(counter >= 50):
        #     # making data frame from csv file
        #     data = pd.read_csv("nba.csv", index_col ="Name")
        #     # dropping passed values
        #     data.drop()
            
            
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        info = {
            "Time": timeLapse,
            "GyroX": sensorValueX,
            "GyroY": sensorValueY,
        }

        csv_writer.writerow(info)
        print(timeLapse, sensorValueX, sensorValueY)

        timeLapse += 1
        sensorValueX = sensorValueX + random.randint(-4, 3)
        sensorValueY = sensorValueY + random.randint(-4, 2)
        counter+=1
        time.sleep(0.5)