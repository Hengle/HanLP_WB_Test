#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

# 分离文本中的行，添加星号。
lines = text.split('\n')

# 每一行都加个星号
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# 重新连成文本
text = '\n'.join(lines)

pyperclip.copy(text)
