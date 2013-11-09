# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals, print_function
from django.contrib.auth.models import User
from django.core.management import BaseCommand
import requests
from hackathon.models import UserProfile

__author__ = 'tchen'

DIRECTORY_API = 'http://api.jcnrd.us/directory/employees.json'


class Command(BaseCommand):
    help = u'Import employee directory'

    def process_user(self, item):
        u, created = User.objects.get_or_create(username=item['uid'])
        p, dummy = UserProfile.objects.get_or_create(user=u)

        # save basic user info
        u.email = item['email']
        first, last = item['preferred_name'].rsplit(' ', 1)
        u.first_name = first
        u.last_name = last
        u.save()

        # save profile info
        p.photo_url = item['photo_url']
        p.cube = item['cube']
        p.ext = item['extension']
        p.mobile = item['mobile']
        p.phone = item['phone']

        try:
            m_first, m_last = item['manager'].rsplit(' ', 1)
            p.manager = User.objects.get(first_name=m_first, last_name=m_last)
        except:
            pass

        p.address = item['address']
        p.department = item['department']
        p.save()

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