#! python3
# coding=gbk
import logging


def foo():
    print('i am foo')
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('foo is running, So should this')
    logging.warning('And this, too')
    logging.error('由于严重的问题，程序的某些功能已经不能正常执行')
    logging.critical('严重的错误，表明程序已不能继续执行')


foo()
