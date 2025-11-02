from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run4(roro:DriveBase, attach):
    sensor = ColorSensor(Port.E) #tod: make sensor part of function
    roro.settings(straight_speed=600)
    roro.use_gyro(True)
    roro.drive(300, 0)
    while sensor.reflection() > 20:
        wait(10)
    roro.straight(10)
    roro.arc(-50, 50)
    roro.arc(50, 50)
    roro.straight(-70)
    for i in range(3):
        roro.straight(-150)
        roro.straight(150)
    roro.arc(50, 90)
    roro.arc(-80, 100)
    roro.straight(750)
        