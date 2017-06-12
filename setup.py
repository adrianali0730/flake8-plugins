from __future__ import with_statement
from setuptools import setup

def get_version(fname='flake8_print.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

install_requires = ['flake8']

setup(
    name='flake8-XPATH',
    description='A flake8 extension that checks for XPATH: statements',
    keywords='flake8 XPATH',
    version='get_version()',
    author='Adrian Ali',
    author_email='adrianali0730@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'UIA200 = flake8_XPATH:XPATH_usage'
        ],
    },
    install_requires=install_requires,
    url='https://github.com/adrianali0730/flake8-plugins',
)
