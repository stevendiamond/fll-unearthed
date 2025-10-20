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
from go import Go
codes = [Go, Go, Go]
hub = PrimeHub()
hub.display.orientation(Side.BOTTOM)
rightMotor = Motor(Port.C)
leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
attach = Motor(Port.A)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
current_code = 0
hub.system.set_stop_button(None)
while True:
    print("at start of while loop")
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)
    print("got to wait")
    wait(333)
    print("got past wait")
    hub.system.set_stop_button(Button.CENTER)
    try:
        print(current_code)
        codes[current_code](robot, attach)
    finally:
        print("got to finally")
        hub.system.set_stop_button(None)
        print("got rid of center button")
        current_code += 1
        current_code %= len(codes)
        robot.use_gyro(False)
        print("got to end of finally")
        wait(333)
        continue
    print("got to end of while loop")