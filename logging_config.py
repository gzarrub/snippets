# -*- coding: utf-8 -*-
import logging.config
import logging
import os
__author__ = 'g.zarrub@gmail.com'

DEFAULT_CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'logging.cfg')
DEFAULT_OUTPUT_FILE = 'report.log'


def logging_config(config=DEFAULT_CONFIG_FILE, output=DEFAULT_OUTPUT_FILE, disable_existing_loggers=True):

    logging.config.fileConfig(config, {'logfilename': output}, disable_existing_loggers)