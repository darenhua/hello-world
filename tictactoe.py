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
X, Y = pyautogui.size()
print(X, Y)

print("Mouse: (%d,%d)" % (MOUSE_X, MOUSE_Y))
print("RGB: %s" % (COLOR[0][1].__str__()))

#print(above.getcolors())
#checks = [above, below, left, right]
count = 0
#for check in checks:
#    if (0,0, 255) in check.getcolors():
#        count += 1
#    if count >= 2:
#        clickable = True


def on_click(x, y, button, pressed):
    tempabove = pyautogui.screenshot(region=(x, y, 10, 60))
    tempright = pyautogui.screenshot(region=(x,y, 60, 10))
    tempbelow = pyautogui.screenshot(region=(x, y, 10, -60))
    templeft = pyautogui.screenshot(region=(x,y, -60, 10))
    print(tempabove.getcolors())
    for i in range(101):
        j = i + 1
        if (j,(0,0,255)) in tempabove.getcolors():
            print('Above detected')
        if (j,(0,0,255)) in tempright.getcolors():
            print('Right detected')
        if (j,(0,0,255)) in tempbelow.getcolors():
            print('Below detected')
        if (j,(0,0,255)) in templeft.getcolors():
            print('Left detected')
        #screenshot does not operate as expected with negative width/heights. The only one I can really use is tempabove.getcolors()

    
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
