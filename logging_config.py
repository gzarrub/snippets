# -*- coding: utf-8 -*-
import extended_config
import logging.config
import logging
import utils
import os
__author__ = 'g.zarrub@gmail.com'



def logging_config(disable_existing_loggers=True):

    properties_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'properties.cfg')
    config = extended_config.ExtendedConfig().read(properties_file)

    config_file = os.path.abspath(config.get('logging', 'config_file'))
    output_file = os.path.abspath(config.get('logging', 'output_file'))

    utils.safe_path(output_file)

    logging.config.fileConfig(config_file, {'logfilename': output_file}, disable_existing_loggers)