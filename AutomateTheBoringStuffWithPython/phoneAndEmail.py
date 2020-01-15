#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# ����绰�����������ʽ
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # �л������ţ�3�����֣������������3������
    (\s|-|\.)?                      # �л��޷ָ�ո񣬻���-������.
    (\d{3})                         # һ����3������
    (\s|-|\.)?                      # �л��޷ָ�ո񣬻���-������.
    (\d{4})                         # һ����4������
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # �л��޷ֻ��ţ�����(�л������ɿո� + һ����ext|x|ext. + �л������ɿո� + һ����2~5������)
)''', re.VERBOSE)

# ��������ʼ���������ʽ
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # �û�������һ�������ַ���ɣ���ʹ�� ��ĸ/����/'.'/'_'/'%'/'+'/'-'
    @                               # @ ����
    [a-zA-Z0-9.-]+                  # ��������һ�������ַ���ɣ���ʹ�� ��ĸ/����/'.'/'-'
    (\.[a-zA-Z]{2,4})               # �� + ��׺����׺�� 2~4 �� ��ĸ ����
)''', re.VERBOSE)

# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
