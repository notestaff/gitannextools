#!/usr/bin/env python

# gitannextools Setup
# Copyright (C) 2019 Ilya Shlyakhter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of version 3 of the GNU General Public License as published by
# the Free Software Foundation
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages
from codecs import open

import versioneer

def readme():
    with open('README.org') as f:
        return f.read()

setup(
    name='gitannextools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='tools for working with git-annex repositories',
    long_description=readme(),
    long_description_content_type='text/org',
    url='https://github.com/notestaff/gitannextools',
    author='Ilya Shlyakhter',
    author_email='ilyawebmail@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='git-annex',
    packages=['gitannextools'],

    install_requires=['future'],
    extras_require={
        'test': ['coverage', 'nose', 'mock'],
    },
)
