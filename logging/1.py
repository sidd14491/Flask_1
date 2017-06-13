import logging

logger = logging.getLogger(__name__)
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
def foo():
    logger.debug('Hi, foo')

class Bar(object):
    def bar(self):
        logger.warn('Hi, bar')
foo()
op= Bar()
op.bar()
