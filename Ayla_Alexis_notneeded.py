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

robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
robot.use_gyro(True)
robot.straight(800)
robot.turn(-90)
robot.straight(65)
robot.turn(-90)
#robot.settings(500)
robot.straight(400)# doing number 9
#robot.settings(200)
robot.straight(-150)
robot.turn(-13)
robot.straight(420)
robot.turn(103)
robot.straight(250)# doing the other one
robot.settings(100)
robot.straight(-200)
robot.settings(200)

#for i in range(4):
#    robot.straight(500)
#    robot.turn(90)