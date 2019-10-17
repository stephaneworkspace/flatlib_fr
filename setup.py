#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    flatlibfr translation of const by Stéphane Bressani (s.bressani@bluewin.ch)
"""

from setuptools import setup
from setuptools import find_packages


setup(
    # Project
    name = 'flatlibfr',
    version = '0.0.1.dev4',
    
    # Sources
    packages = find_packages(),
    package_data = {
        'flatlibfr': [
            'resources/README.md',
            'resources/swefiles/*'
        ],
    },
    
    # Dependencies
    install_requires = ['pyswisseph>=2.00.00-2'],
    
    # Metadata
    description = 'Python library for Traditional Astrology',
    url = 'https://github.com/flatangle/flatlib',
    keywords = ['Astrology', 'Traditional Astrology'],
    license = 'MIT',
    
    # Authoring
    author = 'João Ventura (flatangleweb@gmail.com) and Stéphane Bressani for fr translate (s.bressani@bluewin.ch)',
    author_email = 's.bressani@bluewin.ch',
    
    # Classifiers
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 
)
