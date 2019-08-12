import pyautogui, time
import pytesseract
from PIL import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#location: (322,1039)(346.1065)
im = pyautogui.screenshot(region=(9,1003,144,1023))
im.save("screenshot.png")
print(pytesseract.image_to_string("screenshot.png"))
'''
goal = (334,1052)
icon = pyautogui.locateCenterOnScreen('spotify1.png', confidence=.7)
icon = (icon[0],icon[1])
print(icon, pyautogui.position())
time.sleep(1)

distancex = abs(icon[0] - goal[0])
distancey = abs(icon[1] + goal[1])
distance = (distancex,distancey)
if distance < (10,10):
    pyautogui.click(icon)
else:
    print(distance)
'''
