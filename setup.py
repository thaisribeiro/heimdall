#!/usr/bin/env python

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as fp:
    README = fp.read()

with open(os.path.join(here, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

excluded_packages = ["docs", "tests", "tests.*"]

setup(
    name='heimdall_bank_validate',
    version=VERSION,
    description="Python implementation for bank account validation.",
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='heimdall bank validate',
    author='Thais Ribeiro',
    author_email='thaisribeirodn@gmail.com',
    url='https://github.com/thaisribeiro/heimdall',
    license='MIT License',
    packages=find_packages(exclude=excluded_packages),
    platforms=["any"],
    python_requires=">=3.5"
)