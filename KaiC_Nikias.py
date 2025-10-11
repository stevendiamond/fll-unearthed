#Nikias and Kai. C program works 10/10 for the first part /10 fro the second part  

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

print(robot.settings())
attach.run_until_stalled(10000,duty_limit=60)
attach.control.limits(2000,20000,1000)
robot.settings(straight_speed=450)
robot.straight(500)
robot.arc(200,90)
robot.straight(150 )
robot.turn(-90)
robot.straight(-45)
attach.run_until_stalled(-20000, duty_limit=60)
robot.straight(20)

attach.run_angle(10000,375) #minecart
attach.dc(100)
wait(500)
attach.stop()
attach.run_angle(2000,500)
robot.turn(50)
robot.straight(240)
robot.turn(90)
attach.run_angle(10000,-500)
robot.straight(370)
robot.turn(-370)
robot.straight(-20)
attach.run_until_stalled(-10000, duty_limit=60)    
robot.straight(150)
robot.turn(175)
attach.run_angle(10000,400)






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