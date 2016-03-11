# -*- coding: utf-8 -*-
import logging.config
import logging
import os
__author__ = 'g.zarrub@gmail.com'


DEFAULT_LOG_CONFIG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'logging.cfg')
DEFAULT_LOG_FILE_NAME = 'report.log'

logging.config.fileConfig(DEFAULT_LOG_CONFIG_PATH, {'logfilename': DEFAULT_LOG_FILE_NAME}, True)

def get_basic_logger():
    return logging.getLogger('default')


def get_logger():
    return logging.getLogger(__name__)