import time
# from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import pyautogui


mouse = Controller()
# keyboard = Controller()


def allok_clicker():
    # mouse.position = (48, 400) for small screen
    mouse.position = (367, 535)
    pyautogui.click(clicks=1)
    # mouse.click(Button.left, 1)
    # keyboard.press(Key.enter)


def decr_clicker():
    # mouse.position = (50, 515) for small screen
    mouse.position = (367, 646)
    pyautogui.click(clicks=1)
    # keyboard.press(Key.enter)


def pursuing():
    # findbox x=986,y=84
    pyautogui.hotkey('ctrl', 'f')
    mouse.position = (986, 84)
    mouse.click(Button.left, 1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('backspace')
    time.sleep(0.005)
    pyautogui.typewrite("Pursuing")
    pyautogui.hotkey('enter')


def backclick():
    mouse.position = (1325, 317)
    time.sleep(0.05)
    mouse.click(Button.left, 1)
    time.sleep(2)
