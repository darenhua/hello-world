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

above = pyautogui.screenshot(region=(MOUSE_X, MOUSE_Y+50, 1, 50))
below = pyautogui.screenshot(region=(MOUSE_X, MOUSE_Y-50, 1, 50))
left = pyautogui.screenshot(region=(MOUSE_X+50, MOUSE_Y, 1, 50))
right = pyautogui.screenshot(region=(MOUSE_X-50, MOUSE_Y, 1, 50))

checks = [above, below, left, right]
count = 0
for check in checks:
    if check.getcolors() == (75, 76, 169):
        count += 1
    if count >= 2:
        clickable = True


def on_click(x, y, button, pressed):
    print('Mouse Clicked')
    
def createBoard():
    global board
    board = ''
    board += '     |     |     \n'
    board += '     |     |     \n'
    board += '     |     |     \n'
    board += '-----------------\n'
    board += '     |     |     \n'
    board += '     |     |     \n'
    board += '     |     |     \n'
    board += '-----------------\n'
    board += '     |     |     \n'
    board += '     |     |     \n'
    board += '     |     |     \n'

def clickable(playerTurn):
    pass
def markX(playerTurn):
#    if playerTurn == True:
    pass    
       
createBoard()
print(board)

with Listener(on_click=on_click) as listener:
    listener.join()
