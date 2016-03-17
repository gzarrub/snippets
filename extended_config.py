from ConfigParser import ConfigParser
import logging
import os
__author__ = 'g.zarrub@gmail.com'


class ExtendedConfig:

    def __init__(self, extended=True):
        self.__config__ = ConfigParser()
        self.__extended__ = extended

    def read(self, *config_files):
        """Reads properties files, saves the properties to a config object and overrides its values using environment
        variables with format section_option

        :param config_files:
        :returns: config object
        """

        logger = logging.getLogger(__name__)

        for conf_file in config_files:
            if len(self.__config__.read(conf_file)) == 0:
                message = 'Properties config file not found: %s' % conf_file
                logger.error(message)
                raise Exception(message)

            else:
                logger.debug('Reading properties from file: %s' % conf_file)

        if self.__extended__:
            for section in self.__config__.sections():
                for option in self.__config__.options(section):
                    if "%s_%s" % (section, option) in os.environ:
                        self.__config__.set(section, option, os.environ["%s_%s" % (section, option)])

        return self.__config__