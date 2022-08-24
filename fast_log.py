import logging
from functools import wraps
logging.basicConfig(level=logging.DEBUG, filename='mylog.log')
@wraps(logging.info)
def info_log_and_print(msg, **kwargs):
    print(msg)
    logging.info(msg, **kwargs)
log_fast = info_log_and_print
