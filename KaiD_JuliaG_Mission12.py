from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run6(roro, attach):
    roro.settings(straight_speed=450)
    roro.use_gyro(False)

    attach.run_until_stalled(450,duty_limit=40)
    # roro.straight(250)
    # attach.run_until_stalled(-450,duty_limit=40)
    # roro.straight(-200)
    # roro.straight(40)
    # attach.run_until_stalled(450,duty_limit=40)
    # roro.straight(-500)
    # wait(3000)
    roro.straight(650)
    roro.straight(-1900)