import pyautogui
import time
time.sleep(10)
list1=[[1,1,1,1,0],[0,1,0,1,1,0],[1,0,1,1,0,0]]
for i in list1:
    for k in i:
        if k == 1:
            pyautogui.click() 
        for m in range(10):
            pyautogui.press("right")