# -*- coding: utf-8 -*-
import os
__author__ = 'g.zarrub@gmail.com'


def clean_screen():
    os.system("cls") if os.name in ["ce", "nt", "dos"] else os.system("clear")
