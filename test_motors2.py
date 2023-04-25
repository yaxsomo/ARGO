from pymavlink import mavutil
from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import math
import exceptions
import socket
import argparse



def connectToDrone():
    # Define command line arguments
    parser = argparse.ArgumentParser(description='Motor Test for PixHawk')
    parser.add_argument('--port', type=str, default='/dev/ttyTHS0', help='Serial port for PixHawk (default: /dev/ttyTHS0)')
    args = parser.parse_args()


    baud_rate = 57600

    # Connect to PixHawk
    vehicle = connect(args.port,baud_rate,wait_ready=True)
    return vehicle

def arm():
    while vehicle.is_armable==False:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    print("Vehicle armed!!")
    print("")

    vehicle.armed = True
    while vehicle.armed==False:
        print("Waiting for the drone to become armed")
        time.sleep(1)

    print("Drone is now armed!!!")
    print("Propellers spinning")

    return None


vehicle = connectToDrone()
arm()
print("end of script")
