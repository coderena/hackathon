# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
import logging

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class Hackathon(models.Model):
    class Meta:
        app_label = 'hackathon'
        db_table = 'hackathon_hackathon'
        verbose_name = 'Hackathon'
        ordering = ['-created']
        get_latest_by = 'created'

    name = models.CharField('Name', max_length=24, unique=True)
    slogan = models.CharField('Slogan', max_length=256)
    template = models.CharField('Template', max_length=32, default='default')
    slug = models.CharField('Team Slug', max_length=24, unique=True)
    cover = models.ImageField('Cover', upload_to='hackathons')
    start = models.DateTimeField('Start')
    end = models.DateTimeField('End')
    instruction = models.TextField('Instructions', help_text='Please input the content with markdown syntax')
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.slug:
            self.slug = slugify(self.name)
        super(Hackathon, self).save(force_insert, force_update, using, update_fields)