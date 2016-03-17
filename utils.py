# -*- coding: utf-8 -*-
import os
import re
__author__ = 'g.zarrub@gmail.com'


def clean_screen():

    os.system("cls") if os.name in ["ce", "nt", "dos"] else os.system("clear")


def get_extension(path):

    match = re.match('\..*', os.path.splitext(path)[-1])
    if match is not None:
        return match.groups()

    return None

def is_file(path):
    print get_extension(path)
    if not os.path.exists(path):
        if re.match('\..*', os.path.splitext(path)[-1]) is not None:
            return True

    return os.path.isfile(path)


def safe_path(path):

    if is_file(path):

            not os.path.exists(path):
        if re.match('\..*', os.path.splitext(path)[-1]) is not None:
            path = os.path.dirname(path)

        if not os.path.exists(path):
            os.makedirs(path)