#!/usr/bin/env python

from setuptools import setup, find_packages
from trackma import utils

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "Trackma"
REQUIREMENTS = []
EXTRA_REQUIREMENTS = {
    'curses': ['urwid'],
    'GTK' : ['PyGTK', 'pil-or-pillow'],
    'Qt': ['PyQt4', 'pil-or-pillow'],
}

setup(
    name=NAME,
    version=utils.VERSION,
    packages=find_packages(),
    
    install_requires=REQUIREMENTS,
    extras_require=EXTRA_REQUIREMENTS,
    package_data={'trackma': ['data/*']},

    author='z411',
    author_email='z411@krutt.org',
    description='Open multi-site list manager',
    long_description=read('README.md'),
    url='https://github.com/z411/trackma',
    keywords='list manager, curses, gtk, qt, myanimelist, hummingbird, vndb',
    license="GPL-3",
    entry_points={
        'console_scripts': [
            'trackma = trackma.ui.cli:main',
            'trackma-curses = trackma.ui.curses:main',
        ],
        'gui_scripts': [
            'trackma-gtk = trackma.ui.gtkui:main',
            'trackma-qt = trackma.ui.qtui:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ]
    )
