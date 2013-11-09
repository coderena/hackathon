# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.contrib.auth.models import User
import ldap
from django.conf import settings

__author__ = 'tchen'
logger = logging.getLogger(__name__)


def ldap_auth(dn, secret):
    l = ldap.initialize(settings.LDAP_SERVER)
    l.set_option(ldap.OPT_REFERRALS, 0)
    l.protocol_version = 3
    try:
        l.simple_bind_s(dn, secret)
        return True
    except ldap.INVALID_CREDENTIALS:
        return False

def format_dn(username):
    if username.find(settings.LDAP_SUFFIX) > 0:
        dn = username
        user = dn.replace(settings.LDAP_SUFFIX, '')
    else:
        dn = username + settings.LDAP_SUFFIX
        user = username
    return dn, user


class LDAPBackend(object):
    def authenticate(self, username=None, password=None):
        dn, username = format_dn(username)
        if ldap_auth(dn, password):
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username, is_active=True)
                user.save()
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


