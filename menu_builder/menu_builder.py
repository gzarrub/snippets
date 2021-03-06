# -*- coding: utf-8 -*-
import snippets.helpers.helpers
import logging
__author__ = 'g.zarrub@gmail.com'


class Menu:

    def __init__(self, menu_name):

        self.name = str(menu_name)
        self.message = '\nChoose an option (Press 0 to exit): '
        self.__parent_menu__ = None
        self.options = []

        self.__logger__ = logging.getLogger('file')
        self.__logger__.debug('New menu %s created.' % self.name)

    def add_option(self, message, option, *args, **kwargs):

        self.options.append({'str': message, 'option': True, 'exec': option, 'args': args, 'kwargs': kwargs})
        self.__logger__.debug('New option %s added to menu %s ==> %s()' % (message, self.name, option.__name__))

        return self

    def add_sub_menu(self, menu_name):

        sub_menu = Menu(menu_name)
        sub_menu.message = '\nChoose an option (Press 0 to go parent menu): '
        sub_menu.__parent_menu__ = self
        self.options.append({'str': menu_name, 'option': False, 'exec': sub_menu.get_menu, 'args': [], 'kwargs': {}})

        return sub_menu

    def __show__menu__(self):

        snippets.helpers.clean_screen()
        print '\n%s' % self.name
        for i in range(len(self.options)):
            print "   %d. %s " % (i + 1, self.options[i]['str'])

        return self

    def get_menu(self):

        self.__show__menu__()
        user_option = None

        try:
            user_option = input(self.message)
            self.__logger__.info('Option %d selected.' % user_option)

        except NameError as error:
            self.__logger__.error(error)
            self.get_menu()

        if user_option == 0:
            if self.__parent_menu__ is None:
                self.__logger__.debug('Exiting from menu %s...' % self.name)
                return True

            else:
                self.__logger__.debug('Coming back to parent menu %s...' % self.__parent_menu__.name)
                return self.__parent_menu__.get_menu()

        else:
            if user_option not in range(len(self.options) + 1):
                self.__logger__.debug('Option selected not found.')
                self.get_menu()

            else:
                option = self.options[user_option - 1]
                if option['option']:
                    snippets.helpers.clean_screen()
                    print snippets.helpers.get_title(option['str'])
                    self.__logger__.debug('Selected option %s.' % option['str'])

                option['exec'](*option['args'], **option['kwargs'])

                if option['option']:
                    raw_input('Press any key to continue.')
                    self.get_menu()
