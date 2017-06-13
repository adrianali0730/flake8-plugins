#!/usr/bin/env python

import re

__version__ = '1.0'

CHECKS = [
    (re.compile(r"(By.CSS_SELECTOR)"), 'UIA201', 'Remove temporary selection "checked".')
]


def flake8_MediaMath(f):
    """Decorate flake8 extension function."""
    f.name = 'flake8-MediaMath'
    f.version = __version__
    return f


@flake8_MediaMath
def statement_usage(logical_line, noqa=None):
    if noqa:
        return
    for regexp, code, message in CHECKS:
        match = regexp.search(physical_line)
        if match is not None:
            yield match.start(), '{0} {1}'.format(code, message)
            return
