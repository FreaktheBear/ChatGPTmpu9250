from machine import Pin, I2C
import time
from mpu9250 import MPU9250

# Initialize I2C on Raspberry Pi Pico (SCL on GP5, SDA on GP4)
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Create MPU9250 object
mpu = MPU9250(i2c)

# Main loop to read and display sensor data
while True:
    accel, gyro, mag = mpu.read_all()

    # Display accelerometer data (X, Y, Z in g)
    print("Accelerometer (g): X={:.2f}, Y={:.2f}, Z={:.2f}".format(*accel))

    # Display gyroscope data (X, Y, Z in °/s)
    print("Gyroscope (Deg/s): X={:.2f}, Y={:.2f}, Z={:.2f}".format(*gyro))

    # Display magnetometer data (X, Y, Z in µT)
    print("Magnetometer (muT): X={:.2f}, Y={:.2f}, Z={:.2f}".format(*mag))

    time.sleep(1)  # Wait for 1 second before reading again