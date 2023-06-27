''' fish.py will fish for you; using the controller will let you fish without
Destiny being the active window.

All coordinates given here are for a 1440p, 21:9 monitor.

This needs to be started while standing at the dock with the prompt at the bottom
of your screen.

TODO: Test if it's possible to calculate the position of the watched pixels
without hardcoding them.
'''

import inputs
import time
from ctypes import windll

def fish(controller=False):
    FISH_BUFF = (84, 870)
    FISH_COLOR = 10416786
    dc = windll.user32.GetDC(0)
    def getpixel(x,y):
        return windll.gdi32.GetPixel(dc, x, y)
    if controller:
        input_device = inputs.GamePad()
        CATCH_PROMPT = (1195, 985)
        PROMPT_COLOR = 14389364
        WAIT_TIME = .03 # 30fps - Windows default when game is not the active window
    else:
        input_device = inputs.MnK()
        CATCH_PROMPT = (1189, 984)
        PROMPT_COLOR = 16777215
        WAIT_TIME = .1
    def squaredance(t):
        input_device.move_forward(t)
        input_device.move_left(t)
        input_device.move_backward(t)
        input_device.move_right(t+1)
    time.sleep(2) # Time to alt-tab into the game
    while True:
        input_device.interact(.75)
        while getpixel(*CATCH_PROMPT) != PROMPT_COLOR:
            time.sleep(WAIT_TIME)
        input_device.interact(.5)
        time.sleep(1.5)
        if getpixel(*FISH_BUFF) != FISH_COLOR:
            print(getpixel(*FISH_BUFF))
            squaredance(1)
            squaredance(1)
            break
        input_device.open_map() # Check if Public Event coming
        input_device.back_out()
        time.sleep(1)
        input_device.aim(1) # Anti-AFK
