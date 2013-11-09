# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django import forms

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class ComparisonForm(forms.Form):
    before = forms.CharField(label="Counter Before", widget=forms.Textarea)
    after  = forms.CharField(label="Counter After", widget=forms.Textarea)