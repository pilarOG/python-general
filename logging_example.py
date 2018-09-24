# https://www.udemy.com/python-beyond-the-basics-object-oriented-programming/learn/v4/t/lecture/2599394?start=0

# Example of logging module

import logging

logging.basicConfig(format = '%(asctime)s  %(levelname)s:%(message)s', datfmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.debug('This should be ignored')
logging.info('This message will be printed')
logging.warning('And this too')
