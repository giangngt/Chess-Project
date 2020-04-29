import time
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Controller
keyboard = Controller()
time.sleep(1)
mouse.position = (428, 400)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(2)
keyboard.press('q')
keyboard.release('q')
time.sleep(0.5)
mouse.position = (428, 500)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(2)
mouse.position = (600, 712)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position = (428, 600)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)






