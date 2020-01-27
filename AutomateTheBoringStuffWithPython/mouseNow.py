#! python3
# coding=gbk
import pyautogui
import time

print('Press Ctrl-C to quit.')


def show_mouse_position():
    x, y = pyautogui.position()
    position_str = 'X=' + str(x).rjust(4) + '; Y=' + str(y).rjust(4)
    print(position_str, end='')
    time.sleep(0.25)
    print('\b' * len(position_str), end='', flush=True)


try:
    while True:
        pyautogui.click(1000, 200)
        show_mouse_position()

        pyautogui.click(1000, 500)
        show_mouse_position()

except KeyboardInterrupt:
    print('\nDone.')  # 按下 Ctrl + C 即打印 'Done.'
