# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.views.generic import FormView
from forms import RSIForm
from __init__ import __info__

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class RSIView(FormView):
    template_name = 'rsi.html'
    form_class = RSIForm

    def get_context_data(self, **kwargs):
        context = super(RSIView, self).get_context_data(**kwargs)
        context['info'] = __info__
        return context

    def form_valid(self, form):
        rsi = form.cleaned_data['rsi']
        result = ''
        return self.render_to_response({
            'result': result,
            'info': __info__,
            })