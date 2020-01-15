#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # ���ţ�3�����֣������������3�����֣����߲�����
    (\s|-|\.)?                      # �ո񣬻���-������.�����߲�����
    (\d{3})                         # ǰ3������
    (\s|-|\.)                       # �ո񣬻���-������.
    (\d{4})                         # ��4������
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # �л��޷ֻ���(�л������ɿո� + �����ڵ�ext����x����ext. + �л������ɿո� + 2~5������)
)''', re.VERBOSE)


# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
