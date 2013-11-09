__author__ = 'tchen'

from django.conf.urls import patterns, url

from views import ComparisonView


urlpatterns = patterns('',
                        url(r'^comparison/$', ComparisonView.as_view(), name='comparison')
)
