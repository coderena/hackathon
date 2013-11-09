# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hackathon'
        db.create_table(u'hackathon_hackathon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('template', self.gf('django.db.models.fields.CharField')(default=u'default', max_length=32)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'hackathon', ['Hackathon'])

        # Adding model 'Project'
        db.create_table(u'hackathon_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('hackathon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.Hackathon'])),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('members', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=480)),
            ('information', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'hackathon', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Hackathon'
        db.delete_table(u'hackathon_hackathon')

        # Deleting model 'Project'
        db.delete_table(u'hackathon_project')


    models = {
        u'hackathon.hackathon': {
            'Meta': {'ordering': "[u'-created']", 'object_name': 'Hackathon'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'hackathon.project': {
            'Meta': {'ordering': "[u'created']", 'object_name': 'Project'},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {}),
            'members': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '480'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['hackathon']