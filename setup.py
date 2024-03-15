from setuptools import setup

from file_manager import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/PrabhashDiss/file_manager',
    author='Prabhash Dissanayake',
    author_email='prabhashdissanayake2k@gmail.com',

    py_modules=['file_manager'],
)
