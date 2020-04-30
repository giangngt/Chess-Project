import time
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Controller
keyboard = Controller()
time.sleep(1)
mouse.position = (428, 438)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(2)
keyboard.press('q')
keyboard.release('q')
time.sleep(0.5)
mouse.position = (428, 538)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(2)
mouse.position = (600, 750)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position = (428, 638)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)






