# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
import logging

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class Project(models.Model):
    class Meta:
        app_label = 'hackathon'
        db_table = 'hackathon_project'
        verbose_name = 'Project'
        ordering = ['created']

    name = models.CharField('Project Name', max_length=24, unique=True)
    hackathon = models.ForeignKey('Hackathon', verbose_name='Hackathon')
    cover = models.ImageField('Cover', upload_to='projects')
    abstract = models.CharField('Abstract', max_length=300)
    members = models.CommaSeparatedIntegerField('Members', max_length=480)
    information = models.TextField('Details', help_text='Please input the content with markdown syntax')
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()