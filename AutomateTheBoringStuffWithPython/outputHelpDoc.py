#! python3
# coding=gbk
import sys
import pydoc


def output_help_to_file(filepath, request):
    f = open(filepath, 'w')
    sys.stdout = f
    pydoc.help(request)
    f.close()
    sys.stdout = sys.__stdout__
    return


output_help_to_file(r'pyautogui.dragRel.txt', 'pyautogui.dragRel')
