from time import sleep
import os
import random
def tap_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))

def do_money_work():
    while True:
        tap_screen(467 * 4, 248 * 4)
        sleep(random.uniform(0.2,0.5))
        tap_screen(388 * 4, 219 * 4)
        sleep(random.uniform(0.2, 0.5))

if __name__ == '__main__':
    do_money_work()