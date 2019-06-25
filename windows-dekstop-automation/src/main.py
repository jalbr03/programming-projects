# Taken from the following documentation:
# https://automatetheboringstuff.com/chapter18/

# For this to work, you need to install the package: PyAutoGUI. To do this:
# Navigate to File > Settings, then go to Project: (project name) > Project Interpreter
# Click on the "+" icon on the far right, and then search for: PyAutoGUI
# Then click the button at the bottom: "Install Package"

import pyautogui
import pymsgbox

numOfLoops = pymsgbox.prompt("How many loops?")

# Capture the position so we can go back to it later
position = pyautogui.position()

for i in range(int(numOfLoops)):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

# Go back to the original position:
pyautogui.moveTo(position.x, position.y, duration=0.25)


# FYI, here are a few useful message boxes:
# pymsgbox.alert("This is an alert")
# result = pymsgbox.confirm("Dude, you sure?")
