from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def runa():
    hub = PrimeHub()

    rightMotor = Motor(Port.C)
    leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

    roro = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
    roro.settings(straight_speed=450)
    roro.use_gyro(True)

    roro.straight(2200)