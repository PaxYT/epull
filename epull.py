import keyboard, pyautogui
from time import sleep
oncheck = True

while True:
    if keyboard.is_pressed('shift') and oncheck:
        pyautogui.write('/pull ')
    if keyboard.is_pressed('ctrl'):
        oncheck = not oncheck
    sleep(0.2)
