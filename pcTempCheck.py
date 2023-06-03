import time
import pyautogui
import pynput
import os

keyIn = ''
count = 0
enabled = True
time_check = 0


def key_action():
    global count
    global keyIn
    global time_check

    if keyIn == 'z':
        if count == 1:
            localtime = time.localtime()
            mStr = time.strftime("%M", localtime)
            mNumber = int(mStr)

            # 每十分鐘吃一次食物
            if mNumber % 5 == 0 and time_check == 0:
                pyautogui.scroll(150)
                pyautogui.mouseDown(button='right')
                time.sleep(3)
                pyautogui.mouseUp(button='right')
                time.sleep(1)
                pyautogui.scroll(-150)
                time_check = time_check + 1

            elif mNumber % 5 != 0 and time_check != 0:
                time_check = 0

            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')
            time.sleep(1)

        elif count == 2:
            # mouse.mouseUp(button='right')
            count = 0
            time_check = 0

    elif keyIn == 'x':
        if count == 1:
            pyautogui.mouseDown(button='left')
        elif count == 2:
            pyautogui.mouseUp(button='left')
            count = 0


def key_set(event):
    global count
    global keyIn
    global enabled

    try:
        key_event = event.get(1)

        if hasattr(key_event.key, 'char') and key_event.key.char == 'z' and enabled:
            # if key_event.key.name == 'f12':
            if keyIn != 'z':
                count = 0
            keyIn = 'z'
            count = count + 1
            time.sleep(0.3)

        # elif key_event.key.name == 'f10':
        elif hasattr(key_event.key, 'char') and key_event.key.char == 'x' and enabled:
            if keyIn != 'x':
                count = 0
            keyIn = 'x'
            count = count + 1
            time.sleep(0.3)

        elif hasattr(key_event.key, 'name') and key_event.key.name == 'f12':
            keyIn = ''
            count = 0
            time_check = 0
            pyautogui.mouseUp(button='left')
            enabled = not enabled
            time.sleep(0.3)

        elif hasattr(key_event.key, 'name') and key_event.key.name == 'right':
            os._exit(0)


    except Exception as err:
        # print(err)
        return


# # # # # # # # # # #
if __name__ == '__main__':
    print("Z   : 間隔一秒左鍵")
    print("X   : 長壓左鍵")
    print("F12 : 失效/開啟功能")
    print("方向鍵右關閉程式")

    while True:
        with pynput.keyboard.Events() as event:
            key_action()
            key_set(event)
