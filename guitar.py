
import wiiGHController
from sonicpi_osc import SonicPiOSCClient


def main():  # main loop function

    guitar = wiiGHController.GuitarHeroController(delay=0.01)
    sonicpi_osc = SonicPiOSCClient(path='/bubbleworks/bleguitar', address='192.168.2.59')

    while 1:
        if guitar.new_data():
            guitar.read_all()
            message = [
                guitar.buttonUp,
                guitar.buttonDown,
                guitar.buttonOrange,
                guitar.buttonBlue,
                guitar.buttonYellow,
                guitar.buttonRed,
                guitar.buttonGreen,
                guitar.buttonPlus,
                guitar.buttonMinus,
                guitar.whammyBar,
                guitar.joystickX,
                guitar.joystickY
            ]
            print(message)
            sonicpi_osc.send(message)


# Main program logic:
if __name__ == '__main__':
    main()
