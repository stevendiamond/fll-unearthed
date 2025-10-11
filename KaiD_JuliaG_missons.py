from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#right motor-C
#left motor-D
#attachment-A
#right color sensor-E
#left color sensor-F

rightMotor = Motor(Port.C)
leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
attach = Motor(Port.A)

roro = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
roro.settings(straight_speed=450)
roro.use_gyro(True)

#1 and 2 missions Sep 7
roro.straight(650)
roro.straight(-35)
roro.turn(-85)
roro.turn(35)
roro.straight(110)
roro.straight(-65)# this was a change from roro.straight(-55)
roro.turn(45)
roro.straight(-800)
# roro.straight(30)
# roro.straight(-50)
# roro.turn(-20)
# roro.straight(-800)

# roro.straight(600)
# roro.turn(-30)
# roro.straight(-50)
# roro.turn(30)
# roro.straight(-800)