#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # 有或无区号，3个数字，或者括号里的3个数字
    (\s|-|\.)?                      # 有或无分割，空格，或者-，或者.
    (\d{3})                         # 一定有3个数字
    (\s|-|\.)?                      # 有或无分割，空格，或者-，或者.
    (\d{4})                         # 一定有4个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 有或无分机号，包含(有或无若干空格 + 一定有ext|x|ext. + 有或无若干空格 + 一定有2~5个数字)
)''', re.VERBOSE)


# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
