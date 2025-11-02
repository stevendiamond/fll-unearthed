from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#hub = PrimeHub()
#hub.display.orientation(Side.BOTTOM)
#rightMotor = Motor(Port.C)
#leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
#attach = Motor(Port.A)
#robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
#run1(robot, attach)




def run1(robot, attach):
    robot.use_gyro(True)
    robot.settings(300)
    robot.straight(550)
    robot.arc(-330,90)
    robot.straight(230)
    robot.turn(-135)
    robot.straight(330) #we hit the pushy thingy
    robot.straight(-100)
    robot.turn(-55)    
    robot.straight(500) #we will go forward to hit number 6 the bolders
    robot.straight(-60)
    robot.turn(90)
    robot.straight(100)#this is where we used too end
    robot.turn(-20)
    robot.straight(170)
    robot.turn(65)
    robot.settings(200)
    robot.straight(205)
    robot.settings(500)
    robot.turn(-75)
    robot.straight(350)
    #robot.turn(-20)
#    robot.straight(600) brings it all the way home

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
    
   
   
   
   
   # robot.straight(758)
   # robot.arc(-150,90)
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