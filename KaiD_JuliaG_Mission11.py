from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run5(roro, attach):
    sensor = ColorSensor(Port.E) #tod: make sensor part of function
    roro.settings(straight_speed=600)
    roro.use_gyro(True)
    roro.drive(300, 0)
    while sensor.reflection() > 20:
        wait(10)
    roro.straight(-30)
    roro.arc(-150, 50)
    roro.turn(50)
    roro.straight(-80)
    for i in range(3):
        roro.straight(-110)
        roro.straight(110)
    roro.arc(50, 90)
    roro.arc(-80, 100)
    roro.straight(750)
        