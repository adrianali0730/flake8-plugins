from setuptools import setup

def get_version(fname='flake8-XPATH.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

setup(
    name='flake8-XPATH',
    description='A flake8 extension that checks for XPATH: statements',
    keywords='flake8 XPATH',
    version=get_version(),
    author='Adrian Ali',
    author_email='adrianali0730@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'B90 = flake8_blind_except:check_blind_except'
        ],
    },
    url='https://github.com/elijahandrews/flake8-blind-except',
    license='MIT',
    py_modules=['flake8_blind_except'],
    zip_safe=False,
)