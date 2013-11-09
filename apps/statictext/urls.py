__author__ = 'tchen'

from django.conf.urls import patterns, url

from views import HelpFileView, DocFileView

MATCH_TEXT = r'(?P<text>[\-_0-9a-zA-Z]+)'

urlpatterns = patterns('django.contrib.flatpages.views',
                        url(r'^help/%s/$' % MATCH_TEXT, HelpFileView.as_view(), name='help'),
                        url(r'^doc/%s/$' % MATCH_TEXT, DocFileView.as_view(), name='doc')
)
