#! python3
# coding=utf-8
# pw.py - An insecure password locker program.
"""
第一行开头的写法"#!"是一种 Unix/Linux 特性，这些操作系统上面的 解释器 指令 允许脚本和数据文件充当系统命令，
无需在调用时由用户指定解释器，从而对用户和其它程序隐藏其实现细节。
假设 /usr/local/bin/foo 中有一以下行开头的 Bourne shell 脚本: #!/bin/sh -x
而它被如此调用（"$"是命令提示符）: $ foo bar
这里的 foo 和 bar 类似我们小时候写作文里面的 小明 和 小红，只是随便起的名字，
该命令的输出等同于: $ /bin/sh -x /usr/local/bin/foo bar
注意：此行在 windows 系统下通常无意义，windows 使用系统环境变量来指定 解释器 的位置。
"""
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # 第一个命令行参数是“账户名”
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + ' 的密码已经复制到剪贴板，直接按 Ctrl + V 即可粘贴到指定位置。')
else:
    print('没有找到 ' + account + ' 账户。')
