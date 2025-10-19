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
attach.control.limits(2000,20000,1000)
#attach.run_until_stalled(2000,duty_limit=30)
robot.straight(-330)
robot.turn(-90)
#robot.turn(15)
robot.straight(-870)
robot.arc(-50,-120)
#robot.turn(40)
#robot.straight(-30)
#robot.turn(60)
#robot.straight(20)
#robot.straight(-70)
#robot.turn(95)
#robot.straight(-30) 
#robot.turn(-95)         
















#attach.run_angle(2000,)











#robot.straight(710)
#robot.straight(-10)
#robot.turn(-45) #this is when it hits the opsticle
#robot.turn(45)
#robot.straight(-800)












#robot.settings(300)
#robot.straight(758)
#robot.arc(-150,90)
#robot.straight(100)
#robot.turn(-90)
#robot.straight(250)#hitting the thing
#robot.straight(-180)
#robot.turn(-55)#we will go forward to hit number 6 the bolders
#robot.straight(500)
#robot.straight(-30)
#robot.turn(80)
#robot.straight(315)
#robot.turn(60)
#robot.settings(100)
#robot.straight(160)
#robot.settings(100)
#robot.straight(-100)
#robot.settings(300)
#robot.turn(-95)
#robot.straight(400)

#robot.turn(-105)
#robot.straight(65)
#robot.turn(-90)
#robot.settings(500)
#robot.straight(400)# doing number 9
#robot.settings(200)
#robot.straight(-150)
#robot.turn(-13)
#robot.straight(420)
#robot.turn(103)
#robot.straight(250)# doing the other one
#robot.settings(100)
#robot.straight(-200)
#robot.settings(200)

#for i in range(4):
#    robot.straight(500)
#    robot.turn(90)
