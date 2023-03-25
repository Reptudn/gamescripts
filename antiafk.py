import pyautogui as gui
import time as t
import random

def walk():
    gui.keyDown('w')
    t.sleep(0.2)
    gui.keyUp('w')
    t.sleep(2)
    gui.keyDown('s')
    t.sleep(0.2)
    gui.keyUp('s')
    
    
    
t.sleep(5)
print('starting..')
    
while True:
    print('walking')
    walk()
    t.sleep(random.randrange(40,60))
    
