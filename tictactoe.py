from __future__ import print_function
import time
from pynput.mouse import Listener
import random
import pyautogui

#START = time.time()
#END = time.time()
#Color of | or -- is rgb(75, 76, 169)?

MOUSE_X, MOUSE_Y = pyautogui.position()
PIXEL = pyautogui.screenshot(region=(MOUSE_X, MOUSE_Y, 1, 1))
COLOR = PIXEL.getcolors()

print("Mouse: (%d,%d)" % (MOUSE_X, MOUSE_Y))
print("RGB: %s" % (COLOR[0][1].__str__()))

def on_click(x, y, button, pressed):
    print('Mouse Clicked')
    
def createBoard():
    global row1,row2,row3,row4,row5
    row1 = [' ', '|', ' ', '|', ' ']
    row2 = ['--', '-', '--']
    row3 = row5 = row1
    row4 = row2

def clickable(playerTurn):
    pass
def markX(playerTurn):
#    if playerTurn == True:
    pass    
       
createBoard()
print(row1, row3, row2)

with Listener(on_click=on_click) as listener:
    listener.join()
