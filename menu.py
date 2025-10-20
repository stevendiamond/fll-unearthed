from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu
from a3mis1 import run1
from awasdeleted2 import run2
from asideone3 import run3
from ahelpwith4 import run4
from KaiD_JuliaG_Mission11 import run5
from KaiD_JuliaG_Missions_1_and_2 import run6
from KaiD_JuliaG_Mission12 import run7
from KaiC_Nikias import run8
from acrossTheMap import runa

hub = PrimeHub()
rightMotor = Motor(Port.C)
leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
attach = Motor(Port.A)
# Make a menu to choose a letter. You can also use numbers.
while True:
    print("started loop")
    selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8", "a")
# Based on the selection, run a program.
    exec("run" + selected + "()")
    robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)
    robot.use_gyro(False)
    print("finished loop")
print("out of loop")
    # if selected == "1":
    #     run1()
    # elif selected == "2":
    #     run2()
    # elif selected == "3":
    #     run3()
    # elif selected == "4":
    #     run4()
    # elif selected == "5":
    #     5()
    # elif selected == "6":
    #     6()
    # elif selected == "7":
    #     7()
    # elif selected == "8":
    #     8()
    # elif selected == "a":
    #     a()
