__author__ = 'tchen'

from django.conf.urls import patterns, url

from views import RSIView


urlpatterns = patterns('',
                       url(r'^rsi/$', RSIView.as_view(), name='rsi')
)
