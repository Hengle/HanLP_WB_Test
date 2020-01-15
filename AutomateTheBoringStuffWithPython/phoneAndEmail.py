#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # 区号，3个数字，或者括号里的3个数字，或者不存在
    (\s|-|\.)?                      # 空格，或者-，或者.，或者不存在
    (\d{3})                         # 前3个数字
    (\s|-|\.)                       # 空格，或者-，或者.
    (\d{4})                         # 后4个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 有或无分机号(有或无若干空格 + 括号内的ext或者x或者ext. + 有或无若干空格 + 2~5个数字)
)''', re.VERBOSE)


# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
