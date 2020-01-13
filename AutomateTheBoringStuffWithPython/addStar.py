#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')        # 分离文本中的行，添加星号。
for i in range(len(lines)):     # 每一行都加个星号
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)         # 重新连成文本

pyperclip.copy(text)
