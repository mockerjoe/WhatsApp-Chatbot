import pyautogui
from time import sleep
import random
import pyperclip
import time

sleep(3)

open = False
runs = True

position1 = pyautogui.locateCenterOnScreen("path of emoji.png", grayscale=True, confidence=.6)
x = position1[0]
y = position1[1]

# erhält nachricht 
def get_message():
    global x, y

    position = pyautogui.locateCenterOnScreen("path of emoji.png",grayscale=True,  confidence=.6)
    x = position[0]
    y = position[1]
    pyautogui.moveTo(x, y, duration=.05)
    sleep(1)
    pyautogui.moveTo(x + 30, y - 70, duration=.05)
    pyautogui.tripleClick()
    pyautogui.rightClick()
    pyautogui.moveRel(12,15)
    pyautogui.click()
    whatsapp_message = pyperclip.paste()
    #print(whatsapp_message)
    pyautogui.click()
    print("Nachricht registriert: " + whatsapp_message)

    return whatsapp_message

# verschickt
def post_response(message):
    global x, y

    position = pyautogui.locateCenterOnScreen("path of emoji.png",grayscale=True,  confidence=.6)
    x = position[0]
    y = position[1]
    pyautogui.moveTo(x + 200, y, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(message, interval=.01)

    print(message)
    #pyautogui.typewrite("\n", interval=.1)

# bearbeitet antwort
def process_response(message):
    if "Ey" in str(message):
        return "Hey there"
    if "vomit" in str(message):
        return "delicious"
    else:
        return "Whats up"

# nach neuen nachrichten checken
def check_for_new_messages():
    global runs

    sleep(2)
    pyautogui.moveTo(x+30, y-55, duration=0.5)
    sleep(2)

    while runs == True:
        # suche nach neuen nachrichten und grünem punkt
        try:
            position2 = pyautogui.locateCenterOnScreen("Path of message.png",grayscale=True,  confidence=.85)

            if position2 is not None:
                pyautogui.moveTo(position2)
                sleep(2)
                pyautogui.moveRel(-100,0, duration=.5)
                sleep(2)
                pyautogui.click()
                sleep(5)

        except(Exception):
            print("Keine neuen Nachrichten")

        if pyautogui.pixelMatchesColor(int(x+30), int(y-55), (32, 44, 51), tolerance=10):
            print("eine neue nachricht.")
            processed_message = process_response(get_message())
            post_response(processed_message)
        
        else:
            print("bisher keine neue nachricht...")

        sleep(5)
            
check_for_new_messages()
