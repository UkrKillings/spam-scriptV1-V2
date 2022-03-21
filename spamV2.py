import time, pyautogui, keyboard

print("Использовать только в ознакамительниз целях!")
tet = input("Ты будешь использовать в ознакомительних целях? ")
print("Ой, да кому ты россказиваешь")

time.sleep(10) # через сколько секунд запуститься скрипт
def spam():
    running = True
    while running:
        f = open('tet_spammer.txt', 'r') # текстовый документ где написано то что будет спамить скрипт!

        for line in f:
            if not keyboard.is_pressed('space'):
                pyautogui.typewrite(line)
                pyautogui.press('enter')
            else:
               runnig = False


spam()