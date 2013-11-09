# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django import forms

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class RSIForm(forms.Form):
    rsi = forms.CharField(label='RSI URL', help_text='Please paste url of the RSI file into the textbox')
