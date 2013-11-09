# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals, print_function
from django.contrib.auth.models import User, Group
from django.core.management import BaseCommand
import codecs
import json
import requests

__author__ = 'tchen'

DIRECTORY_API = 'http://api.jcnrd.us/directory/employees.json'


class Command(BaseCommand):
    help = u'Import employee directory'

    def process_user(self, item):
        u, created = User.objects.get_or_create(username=item['uid'])
        if created:
            u.set_password('abcd1234')

        u.email = item['email']
        first, last = item['preferred_name'].rsplit(' ', 1)
        u.first_name = first
        u.last_name = last
        u.save()
        print('User %s %s.' % (u.username, 'created' if created else 'updated'))


    def handle(self, *args, **options):
        page = 1
        while True:
            data = requests.get(DIRECTORY_API, params={'page': page}).json()
            if not data['items']:
                break

            print('\nProcess page %s\n' % page)
            for item in data['items']:
                self.process_user(item)

            page += 1