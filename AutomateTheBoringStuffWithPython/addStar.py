#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

# �����ı��е��У�����Ǻš�
lines = text.split('\n')

# ÿһ�ж��Ӹ��Ǻ�
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# ���������ı�
text = '\n'.join(lines)

pyperclip.copy(text)
