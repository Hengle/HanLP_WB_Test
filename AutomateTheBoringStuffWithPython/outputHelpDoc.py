#! python3
# coding=utf-8
import sys
import pydoc


def output_help_to_file(filepath, request):
    f = open(filepath, 'w')
    sys.stdout = f
    pydoc.help(request)
    f.close()
    sys.stdout = sys.__stdout__
    return


output_help_to_file(r'help_doc/pyautogui.dragRel.txt', 'pyautogui.dragRel')
output_help_to_file(r'help_doc/pyautogui.txt', 'pyautogui')
