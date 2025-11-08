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

def run6(robot, attach):
    robot.use_gyro(True)

    #print(robot.settings())
    attach.run_until_stalled(20000,duty_limit=60)
    attach.control.limits(2000,20000,1000)
    robot.settings(straight_speed=450)
    robot.straight(500)
    robot.arc(200,90)
    robot.straight(150)
    robot.turn(-90)
    robot.straight(-45)
    attach.run_until_stalled(-20000, duty_limit=80)
    robot.straight(40)

    attach.run_angle(10000,275) #minecart
    #attach.dc(100)
    wait(1000)
    attach.stop()
    attach.run_angle(202000,500)
    robot.turn(50)
    robot.straight(240)
    robot.turn(90)
    attach.run_until_stalled(10000,duty_limit=60)
    attach.run_angle(1000,-340) #(-340 works most of the time for sorbet) this may need to be -360 or -370 for roro
    robot.straight(370)
    robot.turn(-370)
    #robot.straight(-15)
    attach.run_until_stalled(-10000, duty_limit=60)
    #robot.arc(400,90)    
    robot.straight(140)
    robot.turn(165)
    robot.straight(50)
    robot.straight(-20)
    attach.run_angle(10000,500)