import datetime

import microdotphat as mdp


class Clock:
    def __init__(self, brightness: float = 0.1, rotate180: bool = False):
        self.brightness = brightness
        self.rotate180 = rotate180

    def start(self) -> None:
        mdp.set_brightness(self.brightness)
        mdp.set_rotate180(self.rotate180)

    def tick(self) -> None:
        mdp.clear()

        t = datetime.datetime.now()
        if t.second % 2 == 0:
            mdp.set_decimal(2, 1)
            mdp.set_decimal(4, 1)
        else:
            mdp.set_decimal(2, 0)
            mdp.set_decimal(4, 0)

        mdp.write_string(t.strftime('%H%M%S'), kerning=False)
        mdp.show()

    @staticmethod
    def clear():
        mdp.clear()
        mdp.show()
