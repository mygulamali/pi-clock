import signal
import sys
import time

from clock import ClockWithButtons as Clock


def terminate(sig_no, frame):
    Clock.clear()
    sys.exit(0)


signal.signal(signal.SIGTERM, terminate)

clock = Clock(rotate180=True)
clock.start()
while True:
    clock.tick()
    time.sleep(0.05)
