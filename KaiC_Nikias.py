#Nikias and Kai. C program works 10/10 for the first part /10 fro the second part  

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

    # hub = PrimeHub()
    # hub.display.orientation(Side.BOTTOM)
    # rightMotor = Motor(Port.C)
    # leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    # attach = Motor(Port.A)
    # robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)

def run7(robot: DriveBase, attach):
    robot.use_gyro(True)

    #print(robot.settings())
    attach.run_until_stalled(20000,duty_limit=60)
    attach.control.limits(2000,20000,1000)
    robot.settings(straight_speed=450)
    robot.straight(500)
    robot.arc(200,90)
    robot.straight(150)
    robot.turn(-90)
    robot.straight(-60)
    attach.run_until_stalled(-20000, duty_limit=60)
    robot.straight(50)
    robot.drive(-20, 0)
    attach.run_angle(10000,200) #minecart
    robot.stop()
    wait(1000)
    attach.run_angle(20000,150) #release from minecart mission 
    #go backwardss because it gets stuck becasue of robot.drive
    robot.turn(50)
    robot.straight(200)
    robot.turn(70)
    attach.run_until_stalled(10000,duty_limit=60)
    attach.run_angle(1000,-310) 
    robot.straight(370)

    robot.turn(-280) #transition into statue rebuild
    robot.straight(275)
    robot.turn(100)
    robot.straight(-60)
    attach.run_angle(1000,-90)
    robot.straight(120)
    attach.run_angle(1000,100)
    robot.turn(30)
    robot.straight(-100)

    #robot.turn(-370)
    # robot.straight(18)
    # attach.run_until_stalled(-10000, duty_limit=60)
    # robot.arc(400,90)    
    # #robot.straight(140)
    # robot.turn(165)
    # robot.straight(50)
    # robot.straight(-20)
    # attach.run_angle(10000,500)