import keyboard, pyautogui, sys
from time import sleep
oncheck = True

while True:
    if keyboard.is_pressed('shift') and oncheck:
        pyautogui.write('/pull ')
    if keyboard.is_pressed('ctrl'):
        oncheck = not oncheck
    sleep(0.2)
    if keyboard.is_pressed('"'):
        sys.exit()
