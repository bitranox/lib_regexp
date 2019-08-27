# -*- coding: utf-8 -*-
import pathlib

from .lib_regexp import *


def get_version() -> str:
    with open(pathlib.Path(__file__).parent / 'version.txt', mode='r') as version_file:
        version = version_file.readline()
    return version


__title__ = 'lib_regexp'
__version__ = get_version()
__name__ = 'lib_regexp'
