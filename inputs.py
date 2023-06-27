from pynput.keyboard import Controller as kc
from pynput.keyboard import Key
from pynput.mouse import Controller as mc
from pynput.mouse import Button
import vgamepad as vg
import time

class GamePad:
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        self.a = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
        self.b = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
        self.x = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
        self.y = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
        self.start = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
        self.back = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK

    # Liked the idea of just passing a function and the relevant args instead of constantly
    # calling a repeated func + update + sleep + reset + update.
    def controller_input(self, func, *args):
        args = list(args)
        t = args.pop(-1)
        func(*args)
        self.gamepad.update()
        time.sleep(t)
        self.gamepad.reset()
        self.gamepad.update()

    def click(self, button, t):
        self.controller_input(self.gamepad.press_button, button, t)

    def aim(self, t):
        self.controller_input(self.gamepad.left_trigger, 255, t)

    def move_forward(self, t):
        self.controller_input(self.gamepad.left_joystick, 0, 32767, t)

    def move_backward(self, t):
        self.controller_input(self.gamepad.left_joystick, 0, -32767, t)

    def move_right(self, t):
        self.controller_input(self.gamepad.left_joystick, 32767, 0, t)

    def move_left(self, t):
        self.controller_input(self.gamepad.left_joystick, -32767, 0, t)

    def interact(self, t):
        self.click(self.x, t)

    def inventory(self):
        self.click(self.start, .2)

    def ghost(self):
        self.click(self.back, .2)

    def go_to_orbit(self):
        self.ghost()
        self.click(self.b, 5)

    def open_map(self):
        self.click(self.back, 1.5)

    def back_out(self):
        self.click(self.b, .5)

class MnK:
    def __init__(self):
        self.keyboard = kc()
        self.mouse = mc()

    def click(self, mouse, t):
        self.mouse.press(Button.left)
        time.sleep(t)
        self.mouse.release(Button.left)
        
    def aim(self, t):
        self.mouse.press(Button.right)
        time.sleep(t)
        self.mouse.release(Button.right)

    def press(self, key, t):
        self.keyboard.press(key)
        time.sleep(t)
        self.keyboard.release(key)

    def move_forward(self, t):
        self.press('w', t)

    def move_backward(self, t):
        self.press('s', t)

    def move_right(self, t):
        self.press('d', t)

    def move_left(self, t):
        self.press('a', t)

    def interact(self, t):
        self.press('e', t)

    def open_map(self):
        self.press('m', .5)

    def back_out(self):
        self.press(Key.esc, .5)
