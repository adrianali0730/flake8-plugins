from __future__ import with_statement
from setuptools import setup

def get_version(fname='flake8_MediaMath.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


setup(
    name='flake8-MediaMath',
    description='A flake8 extension that provides checks related to MediaMath.',
    keywords='flake8 MediaMath',
    version=get_version(),
    author='Adrian Ali',
    author_email='adrianali0730@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'UIA201 = flake8_MediaMath:statement_usage'
        ],
        'flake8.extension': [
            'UIA200 = flake8_MediaMath:statement_usage'
        ],
    },
    url='https://github.com/adrianali0730/flake8-plugins',
    py_modules=['flake8_MediaMath'],
)
