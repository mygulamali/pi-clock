import datetime

import buttonshim
import microdotphat as mdp

DEFAULT_BRIGHTNESS = 0.1
BRIGHTNESS_STEP = 0.05
MAX_BRIGHTNESS = 1.0
MIN_BRIGHTNESS = 0.0


class Clock:
    def __init__(self, brightness: float = DEFAULT_BRIGHTNESS, rotate180: bool = False):
        self.brightness = brightness
        self.rotate180 = rotate180

    def start(self) -> None:
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

        mdp.set_brightness(self.brightness)
        mdp.show()

    @staticmethod
    def clear():
        mdp.clear()
        mdp.show()


class ClockWithButtons(Clock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_button_handlers()

    def setup_button_handlers(self) -> None:
        @buttonshim.on_press(buttonshim.BUTTON_A)
        def button_a(button, pressed):
            self.decrease_brightness()

        @buttonshim.on_press(buttonshim.BUTTON_B)
        def button_b(button, pressed):
            self.increase_brightness()

    def increase_brightness(self) -> None:
        self.brightness = min(self.brightness + BRIGHTNESS_STEP, MAX_BRIGHTNESS)

    def decrease_brightness(self) -> None:
        self.brightness = max(self.brightness - BRIGHTNESS_STEP, MIN_BRIGHTNESS)
