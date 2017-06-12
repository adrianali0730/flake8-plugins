#!/usr/bin/env python

import re

__version__ = '1.0'

CHECKS = [
    (re.compile(r"By.XPATH"), 'UIA200', 'XPATH statement found.')
]


def flake8_XPATH(f):
    """Decorate flake8 extension function."""
    f.name = 'flake8_XPATH.py'
    f.version = __version__
    return f


@flake8_XPATH
def XPATH_usage(logical_line, noqa=None):
    if noqa:
        return
    for regexp, code, message in CHECKS:
        match = regexp.search(logical_line)
        if match is not None:
            yield match.start(), '{0} {1}'.format(code, message)
            return
