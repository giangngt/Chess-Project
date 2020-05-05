import time
from pynput.mouse import Button, Controller
global moved
mouse = Controller()
time.sleep(1)
'''while True:
    print(mouse.position)'''
#Start the game
mouse.position = (402,434)
time.sleep(0.5)
mouse.press(Button.left)
time.sleep(0.05)
mouse.release(Button.left)
#Pawn movement
mouse.position = (650, 715)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (650, 515)
mouse.release(Button.left)
#Knight movement
time.sleep(5)
mouse.position = (850, 815)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (950, 615)
mouse.release(Button.left)
#Queen Movement
time.sleep(10)
mouse.position = (550, 815)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (750, 615)
mouse.release(Button.left)
#Bishop Movement
time.sleep(20)
mouse.position = (750, 815)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (550, 615)
mouse.release(Button.left)
#Rook Movement
time.sleep(30)
mouse.position = (950, 815)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (750, 815)
mouse.release(Button.left)
#King Movement
time.sleep(30)
mouse.position = (650, 815)
time.sleep(0.5)
mouse.press(Button.left)
mouse.position = (650, 715)
mouse.release(Button.left)