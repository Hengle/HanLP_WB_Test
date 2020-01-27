#! python3
# coding=gbk
import pyautogui
import time

print('Press Ctrl-C to quit.')


def doit():
    x, y = pyautogui.position()
    position_str = 'X=' + str(x).rjust(4) + '; Y=' + str(y).rjust(4)
    print(position_str, end='')
    time.sleep(0.25)
    print('\b' * len(position_str), end='', flush=True)


while True:
    pyautogui.click(1000, 200)
    doit()
    time.sleep(0.25)
    pyautogui.click(1000, 500)
    doit()
    time.sleep(0.25)

"""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X = ' + str(x).rjust(4) + 'Y = ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')  # 按下 Ctrl + C 即打印 'Done.'

"""
