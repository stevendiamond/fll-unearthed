from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run4(roro:DriveBase, attach):
    sensor = ColorSensor(Port.E) #tod: make sensor part of function
    roro.settings(600)
    roro.use_gyro(True)
    roro.straight(800)
    roro.drive(300, 0)
    while sensor.reflection() > 20:
        wait(10)
    roro.straight(30)
    roro.arc(10, 90)
    roro.straight(-150)
    roro.arc(10, -90)
    roro.straight(170)
    for i in range(3):
        roro.straight(-170)
        roro.straight(200)
    roro.straight(-130)
    roro.turn(90)
    roro.arc(-170, 120)
    roro.straight(1000)
        