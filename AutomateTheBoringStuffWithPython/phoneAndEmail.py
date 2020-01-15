#! python3
# coding=gbk
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# ����绰�����������ʽ
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # ��1�飬�л������ţ�3�����֣������������3������
    (\s|-|\.)?                      # ��2�飬�л��޷ָ�ո񣬻���-������.
    (\d{3})                         # ��3�飬һ����3������
    (\s|-|\.)?                      # ��4�飬�л��޷ָ�ո񣬻���-������.
    (\d{4})                         # ��5�飬һ����4������
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # ��6�飬�л��޷ֻ��ţ�(�л������ɿո� + ��7�飬һ����ext|x|ext. + �л������ɿո� + ��8�飬һ����2~5������)
)''', re.VERBOSE)

# ��������ʼ���������ʽ
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # �û�������һ�������ַ���ɣ���ʹ�� ��ĸ/����/'.'/'_'/'%'/'+'/'-'
    @                               # @ ����
    [a-zA-Z0-9.-]+                  # ��������һ�������ַ���ɣ���ʹ�� ��ĸ/����/'.'/'-'
    (\.[a-zA-Z]{2,4})               # �� + �������������������� 2~4 �� ��ĸ ����
)''', re.VERBOSE)

# �ڼ�������ı���Ѱ��ƥ����ı�
text = str(pyperclip.paste())  # ��ȡ�������е��ı�
matches = []  # ���ڴ���ҵ��Ľ��

# �����ı���Ѱ�ҵ绰����
for groups in phoneRegex.findall(text):

    if len(groups[1]) == 0:
        area_code = '000'
    elif len(groups[1]) == 5:
        area_code = groups[1][1:4]
    else:
        area_code = groups[1]

#    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    phoneNum = '-'.join([area_code, groups[3], groups[5]])

    if groups[8] != '':  # ����ɷֻ���
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)  # ����绰����

# �����ı���Ѱ�ҵ����ʼ���ַ
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # ��������ʼ���ַ

# �����������������
if len(matches) > 0:  # ����ҵ���
    pyperclip.copy('\n'.join(matches))  # һ��һ�У����������
    print('Copied to clipboard:')
    print('\n'.join(matches))  # ��ӡ����Ļ��
else:
    print('No phone numbers or email addresses found.')  # û���ҵ�

r'''
������ҳ��https://nostarch.com/contactus ����ҳ��Ctrl+A��Ctrl+C�����б����򣬵õ����½����
(hanlp) E:\Proj_Pycharm\HanLP_Test\AutomateTheBoringStuffWithPython>python phoneAndEmail.py
Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''
