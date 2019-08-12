import pyautogui, time
import pytesseract
from PIL import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#location: (322,1039)(346.1065)
im = pyautogui.screenshot(region=(1183,234,565,91))
im.save("screenshot.png")
print(pytesseract.image_to_string(im))
