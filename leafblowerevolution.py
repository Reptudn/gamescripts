import pyautogui as gui
import time
from pynput import keyboard as input


start_pos = [100, 50]
end_pos   = [1920 - start_pos[0], 1080 - start_pos[1]]
step      = 300
move_dur  = 0.1
wait_time = 10
time_b4_start = 5

global started
started = False 


def start():
    
    print('Starting...')
    time.sleep(time_b4_start)
    setup_farming()    
    
          

#farming
def setup_farming():
    
    gui.moveTo(start_pos[0], start_pos[1], duration=0) #move to default pos top left
    
    while True:
        collector()
        gui.moveTo(end_pos[0], end_pos[1], duration=move_dur) #last column down
        time.sleep(wait_time) 

def collector():
    
    for i in range (0, end_pos[0] - step, step):
        gui.moveTo(i, end_pos[1], duration=move_dur) #column down
        gui.moveTo(i + step, start_pos[1], duration=0.3) #to the right and back up
            
              


#key control listener    
def on_press(key):
    
    started = False
    
    if(key == input.Key.space):
        if(started == False):
            started = True
            start()
        else:    
            print('Exiting...')
            exit()


with input.Listener(on_press=on_press) as listener:
    listener.join()    


