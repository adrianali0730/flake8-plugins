#!/usr/bin/env python

try:
	import pycodestyle
	import re
except:
	import pep8 as pycodestyle
	import re

__version__ = '1.0'

XPATH = re.compile(r'(By.XPATH)')

def check_XPATH(physical_line):
	if pycodestyle.noqa(physical_line):
		return
	match = XPATH.search(physical_line)
	if match:
		return match.start(), 'UIA-200 XPATH except: Use CSS Selectors not XPATH.'

check_XPATH.name = 'flake8-XPATH'
check_XPATH.version = __version__
