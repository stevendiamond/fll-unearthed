from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from a3mis1 import run1
from awasdeleted2 import run2
from asideone3 import run3
from ahelpwith4 import run4
from KaiD_JuliaG_Mission11 import run5
from KaiD_JuliaG_Missions_1_and_2 import run6
from KaiD_JuliaG_Mission12 import run7
from KaiC_Nikias import run8
from acrossTheMap import runa
codes = [run1, run2, run3, run5, run6, run7, run8]
hub = PrimeHub()
rightMotor = Motor(Port.C)
leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
attach = Motor(Port.A)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
for code in codes:
    while Button.LEFT not in hub.buttons.pressed():
        wait(10)
    code(robot, attach)
    robot.use_gyro(False)