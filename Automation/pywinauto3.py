from pywinauto import Desktop, Application
import pyautogui
app = Application().start("mspaint.exe")
width, height = (pyautogui.size())
print(width,height)
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.2)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration = 0.2)
    pyautogui.dragRel(-distance,0,duration = 0.2)
    distance =distance - 5
    pyautogui.dragRel(0,-distance,duration = 0.2)