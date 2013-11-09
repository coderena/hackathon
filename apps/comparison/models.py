# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from itertools import imap
import re

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class Comparison:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __call__(self, *args, **kwargs):
        regex = re.compile(r'-?\d+', re.IGNORECASE)
        i1 = regex.findall(self.before)
        i2 = regex.findall(self.after)
        i3 = imap(lambda a1, b1: str(int(b1) - int(a1)), i1, i2)
        return regex.sub(lambda x: i3.next().ljust(len(x.group(0))), self.after)