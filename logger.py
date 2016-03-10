# -*- coding: utf-8 -*-
from string import get_title
import logging.config
import logging
import os
__author__ = 'g.zarrub@gmail.com'

CONFIG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'conf', 'logger.conf')
LOGFILENAME = 'report.log'

logging.config.fileConfig(CONFIG_PATH, {'logfilename': LOGFILENAME}, True)


def log_title(title, max_length=120, char='#'):
    logging.getLogger('default').debug(get_title(title, max_length, char))
