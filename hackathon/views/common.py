# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import logging
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
import markdown
import re
from hackathon.models import Hackathon
from hackathon.utils.helper import info_response, get_url_by_conf

__author__ = 'tchen'
logger = logging.getLogger(__name__)


def redirect_user(user):
    return HttpResponseRedirect('/')


class IndexView(TemplateView):
    template_name = 'hackathon/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['request'] = self.request

        hackathon = Hackathon.objects.latest()
        context['hackathon'] = hackathon

        context['ad'] = {
            'title': hackathon.name,
            'slogan': hackathon.slogan,
            'extra': 'Start at <span>%s</span>, finish at <span>%s</span>, 48-hour nonstop coding and shipping!',
            'action_url': '/project/register/',
            'action_text': 'Register!'
        }

        return context

class SigninView(TemplateView):
    template_name = 'hackathon/signin.html'

    def get_context_data(self, **kwargs):
        context = super(SigninView, self).get_context_data(**kwargs)
        context['ad'] = {
            'title': 'Hackathon',
        }

        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect_user(user)
            else:
                return info_response('Your account is inactive. Please contact your hiring manager.')
        else:
            return HttpResponseRedirect(get_url_by_conf('signin'))


class SignoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class StaticFileView(TemplateView):
    template_name = 'flatpages/default.html'
    path = ''

    def get_context_data(self, **kwargs):
        context = super(StaticFileView, self).get_context_data(**kwargs)
        from django.conf import settings
        import os
        filename = os.path.join(settings.PROJECT_ROOT, self.path,  self.kwargs['text'] + '.md')
        title, content = re.split('====+', codecs.open(filename, encoding='utf8').read())

        content = markdown.markdown(content)
        context['flatpage'] = {
            'title': title,
            'content': content,
        }

        return context


class HelpFileView(StaticFileView):
    path = 'help'


class DocFileView(StaticFileView):
    path = 'doc'