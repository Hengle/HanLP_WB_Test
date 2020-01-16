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

# TODO: Save clipboard content.

# TODO: List keywords and load content.

mcbShelf.close()
