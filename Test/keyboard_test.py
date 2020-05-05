import time
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
time.sleep(1)
#Start the game
mouse.position = (428, 442)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
#Test H key for AI move
time.sleep(1)
keyboard.press('h')
keyboard.release('h')
#Test E key to evaluate
time.sleep(1)
keyboard.press('e')
keyboard.release('e')
#Test U key to undo
time.sleep(2)
keyboard.press('u')
keyboard.release('u')
#Test C key to change board color
time.sleep(1)
keyboard.press('c')
keyboard.release('c')
#Test M key to mute
time.sleep(1)
keyboard.press('m')
keyboard.release('m')
#Test P key to print move list
time.sleep(1)
keyboard.press('p')
keyboard.release('p')
#Test J for Joker
time.sleep(2)
keyboard.press('j')
keyboard.release('j')
