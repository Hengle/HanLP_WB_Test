#! python3
# coding=gbk
import pyautogui
import time

print('Press Ctrl-C to quit.')

while True:
    x, y = pyautogui.position()
    positionStr = 'X=' + str(x).rjust(4) + '; Y=' + str(y).rjust(4)
    print(positionStr, end='')
    time.sleep(0.2)
    print('\b' * len(positionStr), end='', flush=True)

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
