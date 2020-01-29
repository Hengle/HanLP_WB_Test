#! python3
# coding=gbk
import pyautogui
import time

print('Press Ctrl-C to quit.')


def show_mouse_position():
    x, y = pyautogui.position()
    position_str = 'X=' + str(x).rjust(4) + '; Y=' + str(y).rjust(4)
    print(position_str, end='')
    time.sleep(1.0)
    print('\b' * len(position_str), end='', flush=True)


def test_01():
    while True:
        pyautogui.click(1000, 200)
        show_mouse_position()

        pyautogui.click(1000, 500)
        show_mouse_position()


def test_02():
    time.sleep(5)
    pyautogui.click()  # click to put drawing program in focus
    distance = 200
    du = 0.5
    alpha = 10
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=du, _pause=True)  # move right
        distance = distance - alpha
        pyautogui.dragRel(0, distance, duration=du, _pause=False)  # move down
        distance = distance - alpha
        pyautogui.dragRel(-distance, 0, duration=du, _pause=False)  # move left
        distance = distance - alpha
        pyautogui.dragRel(0, -distance, duration=du, _pause=False)  # move up
        distance = distance - alpha


test_02()
