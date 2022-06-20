# The following code is based upon the Initio python code made to control a 4tronix Initio RPI Drone

# PLEASE DO NOT RUN THIS CODE ON A PI THAT IS NOT SETUP AS AN INITIO DRONE (PiRoCon Ver) AS IT WILL NOT WORK

# ===================================================================================
# Drone Control.py - Ver 0.8.0
#
# Created BY W. D.  June 2022
# Last Update: June 2022
# Last tested on Python Ver 3.10.5
# ===================================================================================

# START OF CODE
import initio  # Importing Initio.py to use PiRoCon interface Made by 4tronix
import keyboard  # Used for keyboard press recognition

# Initialise initio libray
initio.init()

# Debug print bool
DEBUG = False


def log(comment: str):
    """
    Function to print debug msgs

    :param comment: - Debug msg to print
    """
    if DEBUG is True:
        print(comment)


def switchDebug(x: bool):
    newDEBUG = not x
    return newDEBUG


def increaseSpeed(speed: int):
    """
    Increases motor speed by 10 and returns new value.

    :param speed: Current Motor Speed
    :return: speed
    """
    if speed < 100:
        speed = speed + 10
        log("{DEBUG} Speed increased")
        return speed

    else:
        log("{DEBUG} Max Speed Reached")
        return speed


def decreaseSpeed(speed: int):
    """
    Decreases Speed by 10 and returns new value

    :param speed: Current Motor Speed
    :return: speed
    """
    if speed > 10:
        speed = speed - 10
        log("{DEBUG} Speed Decreased")
        return speed

    else:
        log("{DEBUG} Slowest Speed Set")
        return speed


def forward(speed: int):
    """
    Sets motors to forward at given speed

    :param speed:
    """
    initio.forward(speed)
    string = "{DEBUG} forward at ", speed, "% speed"
    log(string)


def reverse(speed: int):
    """
    Sets motors in reverse at given speed

    :param speed:
    """
    initio.reverse(speed)
    string = "{DEBUG} reverse at ", speed, "% speed"
    log(string)


def leftSpin(speed: int):
    """
    Sets motors to stationary left spin at given speed

    :param speed:
    """
    initio.spinLeft(speed)
    string = "{DEBUG} leftSpin at ", speed, "% speed"
    log(string)


def rightSpin(speed: int):
    """
    Sets motors to stationary right spin at given speed

    :param speed:
    """
    initio.spinRight(speed)
    string = "{DEBUG} rightSpin at ", speed, "% speed"
    log(string)


def motorStop():
    """
    Stops All Motors
    """
    initio.stop()
    log("{DEBUG} All motors stopped")


def main():
    global DEBUG    # TODO: Replace with local variable
    speed = 50      # Set to 50% as default

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
            elif keyboard.on_release("-"):
                speed = decreaseSpeed(speed)

            elif keyboard.on_release("="):
                speed = increaseSpeed(speed)

            # Turning Modifiers
            elif keyboard.is_pressed("a"):
                leftSpin(speed)

            elif keyboard.is_pressed("d"):
                rightSpin(speed)

            # TODO: # Explore Modifiers {WIP}

            # Config Modifiers
            elif keyboard.on_release("0"):
                DEBUG = switchDebug(DEBUG)

    except KeyboardInterrupt:  # The following will run if ctrl+C is inputted
        log("{DEBUG} Interrupt Detected Program Stopping")

    finally:  # Initiates program cleanup
        initio.cleanup()
        exit()


main()
