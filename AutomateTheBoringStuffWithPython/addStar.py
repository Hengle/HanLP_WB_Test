#! python3
# coding=gbk

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')        # �����ı��е��У�����Ǻš�
for i in range(len(lines)):     # ÿһ�ж��Ӹ��Ǻ�
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)         # ���������ı�

pyperclip.copy(text)
