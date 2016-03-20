# -*- coding: utf-8 -*-
import snippets.extended_config
import snippets.helpers
import logging.config
import logging
import os
__author__ = 'g.zarrub@gmail.com'


def configure_logger(disable_existing_loggers=True):

    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    properties_file = os.path.join(root_path, 'config', 'properties.cfg')
    config = snippets.extended_config.ExtendedConfig().read(properties_file)

    config_file = os.path.abspath(config.get('logging', 'config_file'))
    output_file = os.path.abspath(config.get('logging', 'output_file'))

    wrong_output = False
    if not snippets.helpers.is_file(output_file):
        wrong_output = True
        output_file = os.path.abspath(os.path.join('log', 'default.log'))

    snippets.helpers.safe_path(output_file)

    logging.config.fileConfig(config_file, {'logfilename': output_file}, disable_existing_loggers)

    if wrong_output:
        msg = 'The output file defined at %s has a not allowed format, changed to %s' % (config_file, output_file)
        logging.getLogger(__name__).warning(msg)