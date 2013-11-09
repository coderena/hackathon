# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import urllib
from django.conf import settings
from django.core.cache import cache
from django.utils.datastructures import SortedDict
import requests
from requests.auth import HTTPBasicAuth
from pw import get_password
from urlparse import urljoin
from bs4 import BeautifulSoup
from __init__ import __info__
from hashlib import md5

__author__ = 'tchen'
logger = logging.getLogger(__name__)
user, password = get_password()

PR_STATS_URL = urljoin(settings.API_SERVER, 'pr_stats.json')

PR_BASE_URL = 'https://gnats.juniper.net/web/default/do-query?adv=1&expr=' + \
              '__expression__' + \
              '&csv=0&columns=state%2Creported-in%2Csubmitter-id%2Ccategory%2Cproblem-level%2Coriginator%2Cresponsible%2Ccustomer-escalation-owner%2Cdev-owner%2Csystest-owner%2Ccustomer%2Carrival-date%2Cclosed-date&op=%26'

HEADER_NAMES = {
    'Category': 'category',
    'Originator': 'originator',
    'Customer': 'customer',
    'Problem-Level': 'level',
    'Responsible': 'responsible',
    'Dev-Owner': 'dev_owner',
    'Submitter-Id': 'submitter',
    'State': 'state',
    'Reported-In': 'reported_in',
    'Customer-Escalation-Owner': 'ce_owner',
    'Arrival-Date': 'arrived_at',
    'Closed-Date': 'modified_at',
    'Systest-Owner': 'qa_owner'
}


def ckey(s):
    return md5(s).hexdigest()


def expr_to_url(expr, quoted=True):
    if not quoted:
        expr = urllib.quote(urllib.unquote(expr))
    return PR_BASE_URL.replace('__expression__', expr)


class PRStats:
    def __init__(self):
        pass

    def get(self):
        data = cache.get(ckey(PR_STATS_URL))
        if not data:
            results = requests.get(PR_STATS_URL).json()
            data = SortedDict()
            for key in __info__['categories']:
                data[key] = []

            for item in results:
                item['quoted_expr'] = urllib.quote(item['expr'])
                item['pr_url'] = expr_to_url(item['expr'], False)
                data[item['category']].append(item)

            cache.set(ckey(PR_STATS_URL), data, 10)

        return data


class PRStat:

    def __init__(self):
        pass

    def _extract(self, tr, td_name='td'):
        return map(lambda x: x.get_text().strip(), tr.findAll(td_name)[2:])

    def get_headers(self, header_tr):
        return map(lambda x: HEADER_NAMES[x], self._extract(header_tr, 'th'))

    def get_pr(self, pr_tr):
        return self._extract(pr_tr)

    def extract(self, html):
        soup = BeautifulSoup(html)
        records = soup.find(id='records')
        tr_list = records.findAll('tr')
        header_tr = tr_list[0]
        header = self.get_headers(header_tr)
        results = []
        for pr_tr in tr_list[1:]:
            pr = self.get_pr(pr_tr)
            results.append(dict(zip(header, pr)))

        return results

    def retrieve(self, expr):
        data = cache.get(ckey(expr))
        if not data:
            url = expr_to_url(expr, False)
            html = requests.get(url, auth=HTTPBasicAuth(user, password)).text
            data = self.extract(html)
            cache.set(ckey(expr), data)
        return data

    def get_url(self, expr):
        return expr_to_url(expr, False)
