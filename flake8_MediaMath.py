#!/usr/bin/env python

import re
import os
from os.path import basename
import math
import sys

__version__ = '1.0'

row = 1

CHECKS = [

    #UIA201
    (re.compile(r':active'), 'UIA201', 'Remove temporary selection "active".'),
    (re.compile(r':checked'), 'UIA201', 'Remove temporary selection "checked".'),
    (re.compile(r':disabled'), 'UIA201', 'Remove temporary selection "disabled".'),
    (re.compile(r':empty'), 'UIA201', 'Remove temporary selection "empty".'),
    (re.compile(r':enable'), 'UIA201', 'Remove temporary selection "enable".'),
    (re.compile(r':first-child'), 'UIA201', 'Remove temporary selection "first-child".'),
    (re.compile(r':first-of-type'), 'UIA201', 'Remove temporary selection "first-of-type".'),
    (re.compile(r':focus'), 'UIA201', 'Remove temporary selection "focus".'),
    (re.compile(r':hover'), 'UIA201', 'Remove temporary selection "hover".'),
    (re.compile(r':in-range'), 'UIA201', 'Remove temporary selection "in-range".'),
    (re.compile(r':invalid'), 'UIA201', 'Remove temporary selection "invalid".'),
    (re.compile(r':lang'), 'UIA201', 'Remove temporary selection "lang".'),
    (re.compile(r':last-child'), 'UIA201', 'Remove temporary selection "last-child".'),
    (re.compile(r':last-of-type'), 'UIA201', 'Remove temporary selection "last-of-type".'),
    (re.compile(r':link'), 'UIA201', 'Remove temporary selection "link".'),
    (re.compile(r':not'), 'UIA201', 'Remove temporary selection "not".'),
    (re.compile(r':nth-child'), 'UIA201', 'Remove temporary selection "nth-child".'),
    (re.compile(r':nth-last-child'), 'UIA201', 'Remove temporary selection "nth-last-child".'),
    (re.compile(r':nth-last-of-type'), 'UIA201', 'Remove temporary selection "nth-last-of-type".'),
    (re.compile(r':nth-of-type'), 'UIA201', 'Remove temporary selection "nth-of-type".'),
    (re.compile(r':only-of-type'), 'UIA201', 'Remove temporary selection "only-of-type".'),
    (re.compile(r':only-child'), 'UIA201', 'Remove temporary selection "only-child".'),
    (re.compile(r':optional'), 'UIA201', 'Remove temporary selection "optional".'),
    (re.compile(r':out-of-range'), 'UIA201', 'Remove temporary selection "out-of-range".'),
    (re.compile(r':read-only'), 'UIA201', 'Remove temporary selection "read-only".'),
    (re.compile(r':read-write'), 'UIA201', 'Remove temporary selection "read-write".'),
    (re.compile(r':required'), 'UIA201', 'Remove temporary selection "required".'),
    (re.compile(r':root'), 'UIA201', 'Remove temporary selection "root".'),
    (re.compile(r':target'), 'UIA201', 'Remove temporary selection "target".'),
    (re.compile(r':valid'), 'UIA201', 'Remove temporary selection "valid".'),
    (re.compile(r':visited'), 'UIA201', 'Remove temporary selection "visited".'),

    #UIA202
    (re.compile(r'\'{1}[^\']*\"{1}.*\"{1}.*\'{1}'), 'UIA202', 'Locators should not contain specific text.'),

    #UIA301
    (re.compile(r'def .*verify.*\('), 'UIA301', 'This method should not contain the word "verify".'),

    #UIA200 (Always needs to stay at the bottom)
    (re.compile(r'By.XPATH'), 'UIA200', 'XPATH statement found. Use CSS Selector instead.') 

]

CHECKS2 = [
]


def flake8_MediaMath(f):
    """Decorate flake8 extension function."""
    f.name = 'flake8-MediaMath'
    f.version = __version__
    return f


@flake8_MediaMath
def statement_usage(physical_line, noqa=None):
    global row 
    if noqa:
        return
    for line in physical_line.split('\0'):
        for regex, code, message in CHECKS:
            match = re.search(regex, line)
            if(match is None):
                if(code == 'UIA200'):
                    row = row + 1
            if match is not None:
                print('./{0}:{1}:{2}: {3} {4}'.format(basename(sys.argv[1]), row , match.start()+1 ,code, message)) 
                if(code == 'UIA200'):
                    row = row + 1

                    