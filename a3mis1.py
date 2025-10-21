from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run1(robot, attach):
    robot.use_gyro(True)
    robot.settings(300)
    robot.straight(758)
    robot.arc(-150,90)
    robot.straight(100)
    robot.turn(-90)
    robot.straight(250)#hitting the thing
    robot.straight(-180)
    robot.turn(-55)#we will go forward to hit number 6 the bolders
    robot.straight(500)
    #robot.straight(-30)
    robot.turn(80)
    robot.straight(315)
    robot.turn(60)
    robot.settings(100)
    robot.straight(160)
    #robot.settings(100)
    robot.straight(-100)
    robot.settings(300)
    robot.turn(-95)
    robot.straight(400)

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