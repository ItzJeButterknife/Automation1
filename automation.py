import pyautogui, time, pytesseract, openpyxl
from PIL import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_distance_and_click(x,y,image):
    goal = (x,y)
    icon = pyautogui.locateCenterOnScreen(image, confidence=.7)
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

def read_area(x1,y1,x2,y2):
    global text
    width = abs(x1-x2)
    height = abs(y1-y2)
    img = pyautogui.screenshot(region=(x1,y1,width,height))
    img.save("screenshot.png")
    text = pytesseract.image_to_string("screenshot.png")

def get_data(row,file):
    global street, number, adress, surname, forname, date
    data = openpyxl.load_workbook(file)
    sheet = data.get_sheet_by_name('Blad1')
    street = sheet['C'+str(row)].value
    number = sheet['D'+str(row)].value
    adress = str(street) + " " + str(number)

    surname = sheet['B'+str(row)].value
    forname = sheet['A'+str(row)].value

    date = sheet['F'+str(row)].value

#hahahalol

get_data(2,"testfile.xlsx")
pyautogui.click(400,1055)
time.sleep(2)
pyautogui.typewrite('\n')
time.sleep(1)
pyautogui.typewrite(surname)
read_area(889,49,1003,70)
print(text)
