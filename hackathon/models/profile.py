# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import logging

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class UserProfile(models.Model):
    class Meta:
        app_label = 'hackathon'
        db_table = 'hackathon_profile'
        verbose_name = 'Profile'

    user = models.OneToOneField(User)
    photo_url = models.URLField('Avatar', null=True)
    cube = models.CharField('Cube', max_length=20, null=True)
    mobile = models.CharField('Mobile Phone', max_length=20, null=True)
    phone = models.CharField('Phone', max_length=20, null=True)
    ext = models.CharField('Ext', max_length=20, null=True)
    address = models.CharField('Address', max_length=120, null=True)
    manager = models.ForeignKey(User, verbose_name='Manager', related_name='subodinates', null=True, default=None)
    department = models.CharField('Department', max_length=64, null=True)




    def __unicode__(self):
        return u'Profile of %s' % self.user.username