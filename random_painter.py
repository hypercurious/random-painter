from win32api import GetSystemMetrics
from os import path
import os
import pyautogui
import time
import random

#name assignement and storage path
print("Leave blank for default values(100, no, a e s t h e t i c, Desktop).\nIf something is wrong, default values will be assigned.")
default_filename = "a e s t h e t i c"
default_savepath = os.environ['USERPROFILE'] + "\Desktop"
number_of_lines = input("Enter number of lines: ")
if not number_of_lines.isdigit():
    number_of_lines = "100"
drawing_type = input("Select drawing type. Lift the pen?(y/n): ")
file_name = input("Enter a filename: ")
save_path = input("Enter save path: ")

#fixing things
restricted_letters = "\/:*?\"<>|"
for i in restricted_letters:
    if file_name.find(i)!=-1:
        file_name = default_filename 
        break;

if file_name[-1] != ')' and not file_name[-2].isdigit() and file_name[-3] !='(':
    file_name = file_name + " (0)"

if not path.exists(save_path):
    save_path = default_savepath

while path.exists(save_path + "\\" + file_name + ".png"):
    temp = str(int(file_name[-2])+1)
    file_name = file_name[:-2] + temp + ')'

#open mspaint from windows menu
pyautogui.press('winleft')
pyautogui.typewrite('paint')
time.sleep(300/1000)
pyautogui.press("enter")
time.sleep(300/1000)

#go fullscreen
pyautogui.hotkey('winleft', 'up')

#x dimensions
xl = 5
xr = GetSystemMetrics(0)-18
x = xr - xl
#y dimensions
yu = 144
yd = GetSystemMetrics(1)-84
y = yd - yu

#drawing functions
def dont_lift():
    for i in range(int(number_of_lines)):
        pyautogui.dragTo(random.randint(xl, xr), random.randint(yu, yd), button='left')
def lift():
    for i in range(int(number_of_lines)):
        pyautogui.dragTo(random.randint(xl, xr), random.randint(yu, yd), button='left')
        pyautogui.moveTo(random.randint(xl, xr), random.randint(yu, yd))

#let pyautogui make an artistic drawing
pyautogui.moveTo((x)/2, (y)/2)
if drawing_type==("y" or "yes"):
    lift()
else:
    dont_lift()
#save the artwork, exit and show Desktop
pyautogui.hotkey('ctrl', 's')
pyautogui.typewrite(file_name)
pyautogui.press('f4')
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(save_path)
for i in range(4):
    pyautogui.press("enter")
time.sleep(100/1000)
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('winleft', 'd')
