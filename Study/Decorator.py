#! python3
# coding=gbk
import logging


def foo():
    print('i am foo')
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('foo is running, So should this')
    logging.warning('And this, too')


foo()
