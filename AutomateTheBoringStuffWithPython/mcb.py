#! python3
# coding=gbk
"""
mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
       py.exe mcb.pyw list - Loads all keywords to clipboard.
"""
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':  # 保存到剪贴板
    mcbShelf[sys.argv[2]] = pyperclip.paste()  # 将剪贴板中的内容保存到 shelve，关键字由第二个参数传递进来
elif len(sys.argv) == 2:  # 有可能是需要从剪贴板读取文本，也有可能是要打印关键字列表
    if sys.argv[1].lower() == 'list':  # 要打印列表
        pyperclip.copy(str(list(mcbShelf.keys())))  # 将关键字列表存入剪贴板
    elif sys.argv[1] in mcbShelf:  # shelve 中有这个关键字
        pyperclip.copy(mcbShelf[sys.argv[1]])  # 将对应的文本拷贝到剪贴板

mcbShelf.close()
