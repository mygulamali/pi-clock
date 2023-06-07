#!/usr/bin/env python

import datetime
import time

import microdotphat as mdp


mdp.set_rotate180(True)
mdp.set_brightness(0.1)

while True:
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

    time.sleep(0.05)
