from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os
import sys
from codecs import open

import sendgrid

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open('README.rst', 'r', 'utf-8') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ''

try:
    with open('HISTORY.rst', 'r', 'utf-8') as f:
        history = f.read()
except FileNotFoundError:
    history = ''


setup(
    name='sendgrid',
    version=sendgrid.__version__,
    description='Python wrapper for sendgrid',
    url='https://gitlab.com/WorldPilot/sendgrid',
    author='Mathijs Mortimer',
    author_email='thiezn@gmail.com',
    license='MIT',
    packages=['sendgrid'],
    install_requires=['requests'],
    keywords='sendgrid',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
