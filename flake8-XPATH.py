#!/usr/bin/env python

import pycodestyle
import ast
import re

__version__ = '1.0'

class Checker(object):

	def __init__(self, tree, filename):
		self.tree = tree

	def check_XPATH(physical_line):
		match = XPATH.search('By.XPATH')
		print ("Works")
		if match:
			return match.start(), 'UIA-200 XPATH except: Use CSS Selectors not XPATH.'

	check_XPATH.name = 'flake8-XPATH'

