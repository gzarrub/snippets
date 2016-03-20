# -*- coding: utf-8 -*-
import os
import re
__author__ = 'g.zarrub@gmail.com'


def clean_screen():

    os.system("cls") if os.name in ["ce", "nt", "dos"] else os.system("clear")


def get_extension(path):

    match = re.match('\..*', os.path.splitext(path)[-1])
    if match is not None:
        return match.group()

    return None


def is_file(path):

    if not os.path.exists(path):
        if get_extension(path) is not None:
            return True

    return os.path.isfile(path)


def safe_path(path):

    if is_file(path):
        path = os.path.dirname(path)

    if not os.path.exists(path):
        os.makedirs(path)



def center_text(text, length):
    """Add a padding for each side of the text to complete the selected length

    :param text:
    :param length:
    :return:
    """

    span1 = ''.join(' ' for i in range((length - len(text))/2))
    span2 = ''.join(' ' for i in range(length - len(text) - len(span1)))

    return '%s%s%s' % (span1, text, span2)


def get_title(text, max_length=120, char='#'):
    """

    :param text:
    :param max_length:
    :param char:
    :return:
    """

    start = '%s ' % char[0]
    end = ' %s' % char[0]
    title = row = ''

    title_sections = text.replace('\n', ' ').split(' ')
    for title_section in title_sections:
        if len(title_section) > max_length:
            msg = 'A section of your text is larger than the max_length parameter.'
            raise ValueError(msg)

    barrier = ''.join('%s' % char[0] for i in range(max_length))
    empty_row = "%s%s%s\n" % (start, center_text('', max_length - (len(start) + len(end))), end)

    title += '\n%s\n%s' % (barrier, empty_row)

    for title_section in title_sections:
        if len(row) + len(' %s' % title_section) <= max_length - (len(start) + len(end)):
            row += ' %s' % title_section
        else:
            title += '%s%s%s\n' % (start, center_text(row, max_length - (len(start) + len(end))), end)
            row = ''

    title += '%s%s%s\n' % (start, center_text(row, max_length - (len(start) + len(end))), end)
    title += '%s%s\n' % (empty_row, barrier)

    return title