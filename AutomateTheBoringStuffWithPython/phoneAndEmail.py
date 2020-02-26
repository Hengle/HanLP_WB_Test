#! python3
# coding=utf-8
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# 构造电话号码的正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # 第1组，有或无区号，3个数字，或者括号里的3个数字
    (\s|-|\.)?                      # 第2组，有或无分割，空格，或者-，或者.
    (\d{3})                         # 第3组，一定有3个数字
    (\s|-|\.)?                      # 第4组，有或无分割，空格，或者-，或者.
    (\d{4})                         # 第5组，一定有4个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 第6组，有或无分机号，(有或无若干空格 + 第7组，一定有ext|x|ext. + 有或无若干空格 + 第8组，一定有2~5个数字)
)''', re.VERBOSE)

# 构造电子邮件的正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # 用户名，由一个或多个字符组成，可使用 字母/数字/'.'/'_'/'%'/'+'/'-'
    @                               # @ 符号
    [a-zA-Z0-9.-]+                  # 域名，由一个或多个字符组成，可使用 字母/数字/'.'/'-'
    (\.[a-zA-Z]{2,4})               # 点 + 顶级域名，顶级域名由 2~4 个 字母 构成
)''', re.VERBOSE)

# 在剪贴板的文本中寻找匹配的文本
text = str(pyperclip.paste())  # 获取剪贴板中的文本
matches = []  # 用于存放找到的结果

# 遍历文本，寻找电话号码
for groups in phoneRegex.findall(text):

    if len(groups[1]) == 0:
        area_code = '000'
    elif len(groups[1]) == 5:
        area_code = groups[1][1:4]
    else:
        area_code = groups[1]

    #    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    phoneNum = '-'.join([area_code, groups[3], groups[5]])

    if groups[8] != '':  # 如果由分机号
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)  # 保存电话号码

# 遍历文本，寻找电子邮件地址
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # 保存电子邮件地址

# 将结果拷贝到剪贴板
if len(matches) > 0:  # 如果找到了
    pyperclip.copy('\n'.join(matches))  # 一个一行，存入剪贴板
    print('Copied to clipboard:')
    print('\n'.join(matches))  # 打印在屏幕上
else:
    print('No phone numbers or email addresses found.')  # 没有找到

r'''
测试网页：https://nostarch.com/contactus 打开网页，Ctrl+A，Ctrl+C，运行本程序，得到如下结果：
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
