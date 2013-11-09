__author__ = 'tchen'

from django.conf.urls import patterns, url

from views import PRStatsView


urlpatterns = patterns('',
                       url(r'^pr_stats/$', PRStatsView.as_view(), name='pr_stats')
)
