# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import logging
from django.http import HttpResponse

from django.views.generic import FormView, TemplateView
from apps.pr_stats.models import PRStats, PRStat

from forms import PRStatsForm
from __init__ import __info__
import requests

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class PRStatsView(TemplateView):
    template_name = 'pr_stats.html'

    def get_context_data(self, **kwargs):
        context = super(PRStatsView, self).get_context_data(**kwargs)
        context['info'] = __info__
        stats = PRStats()
        context['categories'] = stats.get()

        return context

    def get(self, request, *args, **kwargs):
        expr = request.GET.get('expr', '')
        if not expr:
            return super(PRStatsView, self).get(request, *args, **kwargs)

        stat = PRStat()
        data = stat.retrieve(expr)
        return HttpResponse(json.dumps(data))

