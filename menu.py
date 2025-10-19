from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from pybricks.tools import hub_menu

hub = PrimeHub()



# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8","a")

# Based on the selection, run a program.
if selected == "1":
    import a3mis1
elif selected == "2":
    import awasdeleted2
elif selected == "3":
    import asideone3
elif selected == "4":
    import ahelpwith4
elif selected == "5":
    import KaiD_JuliaG_Mission11
elif selected == "6":
    import KaiD_JuliaG_missions
elif selected == "7":
    import KaiD_JuliaG_Missions12
elif selected == "8":
    import KaiC_Nikias
elif selected == "a":
    import acrossTheMap
