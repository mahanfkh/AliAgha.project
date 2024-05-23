import cv2
import pyautogui
import numpy as np
screen= (1000, 2000)
tasvir1=cv2.VideoWriter_fourcc(*"XVID")
khoroji=cv2.VideoWriter("aliiiiq.avi", tasvir1 , 30.0 , screen)
while True:
    tasvir=pyautogui.screenshot()
    dor=cv2.cvtColor(np.array(tasvir),cv2.COLOR_RGB2BGR)
    khoroji.write(dor)
    if cv2.waitKey(1) == ord("q"):
        break

khoroji.release()
cv2.destroyAllWindows()