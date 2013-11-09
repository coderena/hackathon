# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import logging
from django.views.generic import TemplateView
import misaka as m
import re

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class StaticFileView(TemplateView):
    template_name = 'statictext.html'
    path = ''

    def get_context_data(self, **kwargs):
        context = super(StaticFileView, self).get_context_data(**kwargs)
        from django.conf import settings
        import os
        filename = os.path.join(settings.PROJECT_ROOT, self.path,  self.kwargs['text'] + '.md')
        title, content = re.split('====+', codecs.open(filename, encoding='utf8').read())

        content = m.html(content)
        context['flatpage'] = {
            'title': title,
            'content': content,
            }

        return context


class HelpFileView(StaticFileView):
    path = 'help'


class DocFileView(StaticFileView):
    path = 'doc'