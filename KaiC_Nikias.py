#Nikias and Kai. C program works 10/10 for the first part /10 fro the second part  

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run8(robot, attach):
    robot.use_gyro(True)

    print(robot.settings())
    attach.run_until_stalled(10000,duty_limit=30)
    attach.control.limits(2000,20000,1000)
    robot.settings(straight_speed=450)
    robot.straight(500)
    robot.arc(200,90)
    robot.straight(150)
    robot.turn(-90)
    robot.straight(-45)
    attach.run_until_stalled(-20000, duty_limit=30)
    robot.straight(30)

    attach.run_angle(10000,375) #minecart
    attach.dc(100)
    wait(500)
    attach.stop()
    attach.run_angle(1000,500)
    robot.turn(50)
    robot.straight(240)
    robot.turn(90)
    attach.run_until_stalled(10000,duty_limit=30)
    attach.run_angle(10000,-270)
    robot.straight(370)
    robot.turn(-370)
    robot.straight(-15)
    attach.run_until_stalled(-10000, duty_limit=30)    
    robot.straight(140)
    robot.turn(165)
    robot.straight(50)
    attach.run_angle(10000,500)





    #robot.straight(300)      
    #robot.straight(160)
    #robot.turn(-123)
    #robot.straight (28)
    #attach.run_until_stalled(-1000, duty_limit=50)
    #robot.straight(-100)


    #attach.run_angle(2000,-550)



    #for i in range(4):
    #    robot.straight(500)
    #    robot.turn(90)