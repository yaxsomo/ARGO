from dronekit import connect, VehicleMode
import time
# import argparse



# Define command line arguments
# parser = argparse.ArgumentParser(description='Motor Test for PixHawk')
# parser.add_argument('--port', type=str, default='/dev/ttyTHS0', help='Serial port for PixHawk (default: /dev/ttyTHS1)')
# parser.add_argument('--power', type=float, default=0.15, help='Motor test power (0 to 1, where 1 is full throttle) (default: 0.15)')
# parser.add_argument('--duration', type=int, default=5, help='Motor test duration in seconds (default: 5)')
# args = parser.parse_args()

# Connect to the vehicle
connection_string = '/dev/cu.usbmodem11301'
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, baud=115200)

# Calibrate the gyroscope
print('Calibrating gyroscope...')
vehicle.send_calibrate_gyro()
time.sleep(10)  # Wait for the calibration process to complete

# Calibrate the accelerometer
print('Calibrating accelerometer...')
vehicle.send_calibrate_accelerometer()
time.sleep(10)  # Wait for the calibration process to complete

# Set parameters
SPIN_ARM = 0.1
SPIN_MIN = 0.15
DISABLE_VALUE = 0.0
SAFETY_SWITCH = 11 #Hardware safety switch

# print ("\nPrint all parameters (iterate `vehicle.parameters`):")
# for key, value in vehicle.parameters.items():
#     print (" Key:%s Value:%s" % (key,value))

print("Setting ARMING_CHECK to %s" % "Hardware Safety Switch")
vehicle.parameters['ARMING_CHECK'] = SAFETY_SWITCH

print("Setting SPIN_ARM to %s" % SPIN_ARM)
vehicle.parameters['MOT_SPIN_ARM'] = SPIN_ARM
print("Setting SPIN_MIN to %s" % SPIN_MIN)
vehicle.parameters['MOT_SPIN_MIN'] = SPIN_MIN
print("Setting COMPASS 2 to %s" % bool(DISABLE_VALUE))
vehicle.parameters['COMPASS_USE2'] = DISABLE_VALUE
print("Setting COMPASS 3 to %s" % bool(DISABLE_VALUE))
vehicle.parameters['COMPASS_USE3'] = DISABLE_VALUE
print("Setting GPS to %s" % bool(DISABLE_VALUE))
vehicle.parameters['GPS_TYPE'] = DISABLE_VALUE
print("Setting GPS Auto Config to %s" % bool(DISABLE_VALUE))
vehicle.parameters['GPS_AUTO_CONFIG'] = DISABLE_VALUE
print("Setting AHRS GPS Use to %s" % bool(DISABLE_VALUE))
vehicle.parameters['AHRS_GPS_USE'] = DISABLE_VALUE







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
