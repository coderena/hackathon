# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.views.generic import FormView
from forms import ComparisonForm
from models import Comparison
from __init__ import __info__

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class ComparisonView(FormView):
    template_name = 'comparison.html'
    form_class = ComparisonForm

    def get_context_data(self, **kwargs):
        context = super(ComparisonView, self).get_context_data(**kwargs)
        context['info'] = __info__
        return context

    def form_valid(self, form):
        before = form.cleaned_data['before']
        after = form.cleaned_data['after']
        c = Comparison(before, after)
        result = c()
        return self.render_to_response({
            'result': result,
            'info': __info__,
        })