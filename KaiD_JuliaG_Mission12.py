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
# roro.use_gyro(True)

attach.run_until_stalled(450,duty_limit=40)
roro.straight(250)
attach.run_until_stalled(-450,duty_limit=40)
roro.straight(-200)
attach.run_until_stalled(450,duty_limit=40)
roro.straight(-500)
wait(3000)
roro.straight(650)
roro.straight(-1900)