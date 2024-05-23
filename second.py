import pyautogui
for i in range(10):
    pyautogui.click(interval=2) 
    for j in range(10):
        pyautogui.press("left")

for i in range(10):
    pyautogui.click(interval=2) 
    for j in range(10):
        pyautogui.press("down")

for i in range(10):
    pyautogui.click(interval=2) 
    for j in range(10):
        pyautogui.press("right")

for i in range(10):
    pyautogui.click(interval=2) 
    for j in range(10):
        pyautogui.press("up")
