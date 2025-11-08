from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from go import Go

codes = [Go, Go, Go, Go, Go, Go, Go]

hub = PrimeHub()
hub.display.orientation(Side.BOTTOM)
rightMotor = Motor(Port.C)
leftMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
attach = Motor(Port.A)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 55.6, axle_track = 80)

current_code = 0
hub.system.set_stop_button(None)

while True:
    hub.display.char(str(current_code + 1))
    while Button.CENTER not in hub.buttons.pressed():
        while not hub.buttons.pressed():
            wait(10)
        if Button.LEFT in hub.buttons.pressed():
            current_code += 1
            current_code %= len(codes)
            hub.display.char(str(current_code + 1))
            wait(200)
        if Button.RIGHT in hub.buttons.pressed():
            current_code -= 1
            current_code %= len(codes)
            hub.display.char(str(current_code + 1))
            wait(200)
    wait(333)
    hub.system.set_stop_button(Button.CENTER)
    try:
        codes[current_code](robot, attach)
    finally:
        hub.system.set_stop_button(None)
        current_code += 1
        current_code %= len(codes)
        robot.use_gyro(False)
        wait(333)
        continue