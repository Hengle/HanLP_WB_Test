#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

# 分离文本中的行，添加星号。
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

pyperclip.copy(text)
