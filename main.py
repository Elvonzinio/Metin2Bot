import pyautogui
import time
import ctypes

def click3(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.04)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

licznik=1

while 1:
    while 1:
        if pyautogui.locateOnScreen('5/5biale.png', confidence=0.88) != None or pyautogui.locateOnScreen('5/5czerwone.png', confidence=0.88) != None or pyautogui.locateOnScreen('5/5niebieskie.png', confidence=0.88) != None or pyautogui.locateOnScreen('5/5zlote.png', confidence=0.88) != None:
            flag = 5
            print('wykryto 5')
            break
        elif pyautogui.locateOnScreen('4/4biale.png', confidence=0.88) != None or pyautogui.locateOnScreen('4/4czerwone.png', confidence=0.88) != None or pyautogui.locateOnScreen('4/4niebieskie.png', confidence=0.88) != None or pyautogui.locateOnScreen('4/4zlote.png', confidence=0.88) != None:
            flag = 4
            print('wykryto 4')
            break
        elif pyautogui.locateOnScreen('3/3biale.png', confidence=0.88) != None or pyautogui.locateOnScreen('3/3czerwone.png', confidence=0.88) != None or pyautogui.locateOnScreen('3/3niebieskie.png', confidence=0.88) != None or pyautogui.locateOnScreen('3/3zlote.png', confidence=0.88) != None:
            flag = 3
            print('wykryto 3')
            break
        elif pyautogui.locateOnScreen('2/2biale.png', confidence=0.88) != None or pyautogui.locateOnScreen('2/2czerwone.png', confidence=0.88) != None or pyautogui.locateOnScreen('2/2niebieskie.png', confidence=0.88) != None or pyautogui.locateOnScreen('2/2zlote.png', confidence=0.88) != None:
            flag = 2
            print('wykryto 2')
            break
        elif pyautogui.locateOnScreen('1/1biale.png', confidence=0.88) != None or pyautogui.locateOnScreen('1/1czerwone.png', confidence=0.88) != None or pyautogui.locateOnScreen('1/1niebieskie.png', confidence=0.88) != None or pyautogui.locateOnScreen('1/1zlote.png', confidence=0.88) != None:
            flag = 1
            print('wykryto 1')
            break

    time.sleep(0.1)
    if flag == 1:
        click3(968,397)
    elif flag == 2:
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
    elif flag == 3:
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
    elif flag == 4:
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
    elif flag == 5:
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)
        time.sleep(0.05)
        click3(968,397)

    while 1:
        if pyautogui.locateOnScreen('koniec/straciles.png', confidence=0.9) != None or pyautogui.locateOnScreen('koniec/wylowiles.png', confidence=0.9) != None or pyautogui.locateOnScreen('koniec/zdobyles.png', confidence=0.9) != None:
            time.sleep(2)
            break


    if licznik<200:
        click3(614,132)
    elif licznik<400:
        click3(697, 132)
    elif licznik<600:
        click3(782, 132)
    elif licznik<800:
        click3(867, 132)
    licznik=licznik+1
    time.sleep(0.2)
    click3(968,397)
