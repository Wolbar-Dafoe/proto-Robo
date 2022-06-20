# The following code is based upon the Initio python code made to control a 4tronix Initio RPI Drone

# PLEASE DO NOT RUN THIS CODE ON A PI THAT IS NOT SETUP AS AN INITIO DRONE (PiRoCon Ver) AS IT WILL NOT WORK

# ===================================================================================
# Drone Control.py - Ver 0.7
#
# Created BY W. D.  June 2022
# Last Update: June 2022
# Last tested on Python Ver 3.10.5
# ===================================================================================

# START OF CODE
import initio       # Importing Initio.py to use PiRoCon interface Made by 4tronix
import keyboard     # Used for keyboard press recognition

# Initialise initio libray
initio.init()


def increaseSpeed(speed):
    """
    Increases motor speed by 10 and returns new value.

    :param speed: Current Motor Speed
    :return: speed
    """
    if speed < 100:
        speed = speed + 10
        print("{DEBUG} Speed increased")
        return speed

    else:
        print("{DEBUG} Max Speed Reached")
        return speed


def decreaseSpeed(speed):
    """
    Decreases Speed by 10 and returns new value

    :param speed: Current Motor Speed
    :return: speed
    """
    if speed > 10:
        speed = speed - 10
        print("{DEBUG} Speed Decreased")
        return speed

    else:
        print("{DEBUG} Slowest Speed Set")
        return speed


def forward(speed):
    """
    Sets motors to forward at given speed

    :param speed:
    """
    initio.forward(speed)
    print("{DEBUG} Forward at ", speed, " speed")


def reverse(speed):
    """
    Sets motors in reverse at given speed

    :param speed:
    """
    initio.reverse(speed)
    print("{DEBUG} Reverse at ", speed, " speed")


def leftSpin(speed):
    """
    Sets motors to stationary left spin at given speed

    :param speed:
    """
    initio.spinLeft(speed)
    print("{DEBUG} leftSpin at ", speed, " speed")


def rightSpin(speed):
    """
    Sets motors to stationary right spin at given speed

    :param speed:
    """
    initio.spinRight(speed)
    print("{DEBUG} rightSpin at ", speed, " speed")


def motorStop():
    """
    Stops All Motors
    """
    initio.stop()
    print("{DEBUG} All motors stopped")


def main():
    speed = 30

    try:
        while True:
            # Gear Modifiers
            if keyboard.is_pressed("w"):
                forward(speed)

            elif keyboard.is_pressed("s"):
                reverse(speed)

            elif keyboard.is_pressed("esc"):
                motorStop()

            # Speed Modifiers
            elif keyboard.is_pressed("-"):
                speed = decreaseSpeed(speed)

            elif keyboard.is_pressed("="):
                speed = increaseSpeed(speed)

            # Turning Modifiers
            elif keyboard.is_pressed("a"):
                leftSpin(speed)

            elif keyboard.is_pressed("d"):
                rightSpin(speed)

            # TODO: # Explore Modifiers {WIP}
            # keyboard.om_press_key("m" modeSwitch())

    except KeyboardInterrupt:  # The following will run if ctrl+C is inputted
        print("{DEBUG} Interrupt Detected Program Stopping")

    finally:  # Initiates program cleanup
        initio.cleanup()


main()
