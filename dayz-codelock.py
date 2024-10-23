import pyautogui as p
import time
import random

# digits = int(input('How many digits does the codelock have? '))
max = 10**digits - 1
str_max = str(max)

time.sleep(5)

for i in range(max):
    str_num = str(i)
    zeros = len(str_max) - len(str_num)
    for o in range(zeros):
        p.press('0')
    for char in str_num:
        p.typewrite(char)
    p.click()
    for j in range(digits):
        p.press('delete')
    #time.sleep(random.randint(1, 3))


