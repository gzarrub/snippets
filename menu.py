# -*- coding: utf-8 -*-
import __logging__
import string
import __os__
__author__ = 'gzarzuelo'


logger = __logging__.get_logger()


class Menu:
    def __init__(self, menu_str):
        self.__menu_str__ = menu_str
        self.__select_str__ = 'Choose an option (Press 0 to exit): '
        self.__parent_menu__ = None
        self.__menu_options__ = []
        self.__sub_menus__ = []

    def add_option(self, option_str, option, *args, **kwargs):
        self.__menu_options__.append(
            {'str': option_str, 'option': True, 'exec': option, 'args': args, 'kwargs': kwargs}
        )

    def add_sub_menu(self, sub_menu_str):
        sub_menu = Menu(sub_menu_str)
        sub_menu.__parent_menu__ = self
        sub_menu.__select_str__ = 'Choose an option (Press 0 to go parent menu): '
        self.__sub_menus__.append(sub_menu)
        self.__menu_options__.append(
            {'str': sub_menu_str, 'option': False, 'exec': sub_menu.get_menu, 'args': [], 'kwargs': {}}
        )
        return sub_menu

    def set_select_str(self, select_str):
        self.__select_str__ = select_str

    def __show__menu__(self):
        __os__.clean_screen()
        print self.__menu_str__
        for i in range(len(self.__menu_options__)):
            print "   %d. %s " % (i + 1, self.__menu_options__[i]['str'])

    def get_menu(self):

        self.__show__menu__()
        user_option = None

        try:
            user_option = input(self.__select_str__)
        except NameError:
            self.get_menu()

        if user_option == 0:
            return True if self.__parent_menu__ is None else self.__parent_menu__.get_menu()

        else:
            if user_option not in range(len(self.__menu_options__) + 1):
                self.get_menu()
            else:
                option = self.__menu_options__[user_option - 1]
                if option['option']:
                    __os__.clean_screen()
                    print string.get_title(option['str'])

                option['exec'](*option['args'], **option['kwargs'])

                if option['option']:
                    raw_input('Press any key to continue.')
                    self.get_menu()
