from setuptools import setup, find_packages

setup(
    name='file_manager',
    version='0.1',
    packages=find_packages(),
    author='Prabhash Dissanayake',
    author_email='prabhashdissanayake2k@gmail.com',
    description='A Python package for handling files and folders',
    long_description='''\
A Python package for creating and managing file structures from string representations. Includes functions for converting between tree-like and flat representations of file structures.''',
    long_description_content_type='text/plain',
    url='https://github.com/PrabhashDiss/file_manager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
