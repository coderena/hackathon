# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

import logging
logger = logging.getLogger(__name__)

__author__ = 'tchen'


register = template.Library()

@register.inclusion_tag('hackathon/ttags/hackathon_ad.html')
def hackthon_ad(request, ad):
    return {
        'request': request,
        'ad': ad
    }

@register.inclusion_tag('hackathon/ttags/recent_projects.html')
def recent_projects(request, title, project_list):
    return {
        'request': request,
        'title': title,
        'project_list': project_list
    }