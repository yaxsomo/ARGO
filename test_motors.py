from pymavlink import mavutil
from dronekit import connect, VehicleMode, LocationGlobalRelative.APIException
import time
import math
import exceptions
import socket
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Motor Test for PixHawk')
parser.add_argument('--port', type=str, default='/dev/ttyTHS0', help='Serial port for PixHawk (default: /dev/ttyTHS1)')
parser.add_argument('--power', type=float, default=0.15, help='Motor test power (0 to 1, where 1 is full throttle) (default: 0.15)')
parser.add_argument('--duration', type=int, default=5, help='Motor test duration in seconds (default: 5)')
args = parser.parse_args()

# Connect to PixHawk
master = mavutil.mavlink_connection(args.port)

# Define motor test parameters
motor_test_power = args.power  # Motor test power
motor_test_duration = args.duration  # Motor test duration in seconds

# Send motor test command
master.mav.command_long_send(
    target_system=1, target_component=1,
    command=400, confirmation=0,
    param1=5, param2=motor_test_power, param3=0, param4=0, param5=0, param6=0, param7=0
)  # Command to set motor test at given power level for given duration

# Wait for motor test to complete or catch keyboard interrupt
print(f"Motor test started. Press Ctrl+C to stop.")
try:
    start_time = time.time()
    while time.time() - start_time < motor_test_duration:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

# Send stop motor command
master.mav.command_long_send(
    target_system=1, target_component=1,
    command=400, confirmation=0,
    param1=5, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0
)  # Command to stop motor test

print("Motor test completed.")
