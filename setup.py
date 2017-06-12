from setuptools import setup

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
            'UIA-200 = XPATH:Checker'
        ],
    },
    url='https://github.com/adrianali0730/flake8-plugins',
)
