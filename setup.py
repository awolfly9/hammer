# -*- coding=utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'hammer',
    version = '0.0.1',
    keywords = ('pip'),
    description = 'lgq hammer tool',
    long_description = 'lgq hammer tool',
    license = 'MIT Licence',

    url = 'http://awolfly9.com',
    author = 'lgq',
    author_email = 'awolfly9@gmail.com',

    # packages = ['hammer'],
    packages = find_packages(),
    # include_package_data = True,
    platforms = 'any',
    install_requires = [],
    scripts = ['./kill_port'],
)
