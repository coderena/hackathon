# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django import forms

__author__ = 'tchen'
logger = logging.getLogger(__name__)

from __init__ import __info__ as info


class PRStatsForm(forms.Form):
    url = forms.URLField(label='GNATS Query URL', help_text='Please paste url of the GNATS query into the textbox')
    category = forms.ChoiceField(choices=tuple(info['categories']), label='Category',
                                 help_text='Please choose a category that best fit this query in')
