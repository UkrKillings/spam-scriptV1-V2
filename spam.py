import time, pyautogui

time.sleep(5)
f = open('tet_spammer.txt', 'r') # текстовый документ где написано то что будет спамить скрипт!

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')