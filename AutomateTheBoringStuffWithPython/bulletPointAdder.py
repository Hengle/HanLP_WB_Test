#! python3
# coding=gbk
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: �����ı��е��У�����Ǻš�
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*' + lines[i]

pyperclip.copy(text)
