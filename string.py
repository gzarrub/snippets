__author__ = 'g.zarrub@gmail.com'


def get_title(title, max_length=120, char='#'):

    barrier = ''.join('%s' % char for i in range(max_length))
    _start_title_ = '%s ' % char
    _end_title_ = ' %s' % char
    _title_ = ''
    message = ''

    def auto_span():
        length_span1 = (max_length - (len(_start_title_) + len(_end_title_)) - len(_title_))/2
        span1 = ''.join(' ' for i in range(length_span1))
        length_span2 = max_length - (len(_start_title_) + len(_end_title_)) - len(_title_) - length_span1
        span2 = ''.join(' ' for i in range(length_span2))

        return span1, span2

    empty_row = "%s%s%s%s\n" % (_start_title_, auto_span()[0], auto_span()[1], _end_title_)

    message += '\n%s\n%s' % (barrier, empty_row)

    for title_section in title.split(' '):
        if len(_title_) + len(' %s' % title_section) <= max_length - (len(_start_title_) + len(_end_title_)):
            _title_ += ' %s' % title_section
        else:
            message += '%s%s%s%s%s\n' % (_start_title_, auto_span()[0], _title_, auto_span()[1], _end_title_)
            _title_ = ''

    message += '%s%s%s%s%s\n' % (_start_title_, auto_span()[0], _title_, auto_span()[1], _end_title_)
    message += '%s%s\n' % (empty_row, barrier)

    return message