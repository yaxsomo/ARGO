from dronekit import connect, VehicleMode
from pymavlink import mavutil
import time
# import argparse



# Define command line arguments
# parser = argparse.ArgumentParser(description='Motor Test for PixHawk')
# parser.add_argument('--port', type=str, default='/dev/ttyTHS0', help='Serial port for PixHawk (default: /dev/ttyTHS1)')
# parser.add_argument('--power', type=float, default=0.15, help='Motor test power (0 to 1, where 1 is full throttle) (default: 0.15)')
# parser.add_argument('--duration', type=int, default=5, help='Motor test duration in seconds (default: 5)')
# args = parser.parse_args()


connection_string = '/dev/cu.usbmodem11301'

# Connect to the vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, baud=921600)

# Set parameters
SPIN_ARM = 0.1
SPIN_MIN = 0.15
DISABLE_COMPASS = 0.0

# print ("\nPrint all parameters (iterate `vehicle.parameters`):")
# for key, value in vehicle.parameters.items():
#     print (" Key:%s Value:%s" % (key,value))


print("Setting SPIN_ARM to %s" % SPIN_ARM)
vehicle.parameters['MOT_SPIN_ARM'] = SPIN_ARM
print("Setting SPIN_MIN to %s" % SPIN_MIN)
vehicle.parameters['MOT_SPIN_MIN'] = SPIN_MIN
print("Setting COMPASS 2 to %s" % bool(DISABLE_COMPASS))
vehicle.parameters['COMPASS_USE2'] = DISABLE_COMPASS
print("Setting COMPASS 3 to %s" % bool(DISABLE_COMPASS))
vehicle.parameters['COMPASS_USE3'] = DISABLE_COMPASS

# Wait for the parameter values to be set
time.sleep(2)

# Arm the vehicle
print("Arming motors")
vehicle.armed = True
vehicle.mode = VehicleMode("GUIDED")
while not vehicle.armed:
    print(" Waiting for arming...")
    time.sleep(1)

print("Takeoff!")
vehicle.simple_takeoff(2)

# Hover for 5 seconds
time.sleep(5)

# Land the vehicle
print("Landing...")
vehicle.mode = VehicleMode("LAND")
time.sleep(1)

# Disarm the vehicle
print("Disarming...")
vehicle.armed = False

# Close the connection
vehicle.close()
print("Done.")
