from __future__ import print_function
import time
from pololu_drv8835_rpi import motors, MAX_SPEED

motors.motor1.setSpeed(300)
motors.motor2.setSpeed(300)