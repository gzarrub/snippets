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

    wrong_output = False
    if not utils.is_file(output_file):
        wrong_output = True
        output_file = os.path.abspath(os.path.join('log', 'default.log'))

    utils.safe_path(output_file)

    logging.config.fileConfig(config_file, {'logfilename': output_file}, disable_existing_loggers)

    if wrong_output:
        msg = 'The output file defined at %s has a not allowed format, changed to %s' % (config_file, output_file)
        logging.getLogger(__name__).warning(msg)