#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

# �����ı��е��У�����Ǻš�
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

pyperclip.copy(text)
