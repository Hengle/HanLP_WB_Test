#! python3
# coding=gbk
# pw.py - An insecure password locker program.
"""
��һ�п�ͷ��д��"#!"��һ�� Unix/Linux ���ԣ���Щ����ϵͳ����� ������ ָ�� ����ű��������ļ��䵱ϵͳ���
�����ڵ���ʱ���û�ָ�����������Ӷ����û�����������������ʵ��ϸ�ڡ�
���� /usr/local/bin/foo ����һ�����п�ͷ�� Bourne shell �ű�: #!/bin/sh -x
��������˵��ã�"$"��������ʾ����: $ foo bar
����� foo �� bar ��������Сʱ��д��������� С�� �� С�죬ֻ�����������֣�
������������ͬ��: $ /bin/sh -x /usr/local/bin/foo bar
ע�⣺������ windows ϵͳ��ͨ�������壬windows ʹ��ϵͳ����������ָ�� ������ ��λ�á�
"""
import sys
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # ��һ�������в����ǡ��˻�����
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + ' �������Ѿ����Ƶ������壬ֱ�Ӱ� Ctrl + V ����ճ����ָ��λ�á�')
else:
    print('û���ҵ� ' + account + ' �˻���')
