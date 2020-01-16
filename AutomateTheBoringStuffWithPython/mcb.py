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

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':  # ���浽������
    mcbShelf[sys.argv[2]] = pyperclip.paste()  # ���������е����ݱ��浽 shelve���ؼ����ɵڶ����������ݽ���
elif len(sys.argv) == 2:  # �п�������Ҫ�Ӽ������ȡ�ı���Ҳ�п�����Ҫ��ӡ�ؼ����б�
    if sys.argv[1].lower() == 'list':  # Ҫ��ӡ�б�
        pyperclip.copy(str(list(mcbShelf.keys())))  # ���ؼ����б���������
    elif sys.argv[1] in mcbShelf:  # shelve ��������ؼ���
        pyperclip.copy(mcbShelf[sys.argv[1]])  # ����Ӧ���ı�������������

mcbShelf.close()
