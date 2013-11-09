# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.cube'
        db.alter_column(u'hackathon_profile', 'cube', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.mobile'
        db.alter_column(u'hackathon_profile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.ext'
        db.alter_column(u'hackathon_profile', 'ext', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.phone'
        db.alter_column(u'hackathon_profile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.manager'
        db.alter_column(u'hackathon_profile', 'manager_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'UserProfile.address'
        db.alter_column(u'hackathon_profile', 'address', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'UserProfile.department'
        db.alter_column(u'hackathon_profile', 'department', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'UserProfile.photo_url'
        db.alter_column(u'hackathon_profile', 'photo_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UserProfile.cube'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.cube' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.cube'
        db.alter_column(u'hackathon_profile', 'cube', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'UserProfile.mobile'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.mobile' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.mobile'
        db.alter_column(u'hackathon_profile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'UserProfile.ext'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.ext' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.ext'
        db.alter_column(u'hackathon_profile', 'ext', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'UserProfile.phone'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.phone'
        db.alter_column(u'hackathon_profile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'UserProfile.manager'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.manager' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.manager'
        db.alter_column(u'hackathon_profile', 'manager_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # User chose to not deal with backwards NULL issues for 'UserProfile.address'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.address'
        db.alter_column(u'hackathon_profile', 'address', self.gf('django.db.models.fields.CharField')(max_length=120))

        # User chose to not deal with backwards NULL issues for 'UserProfile.department'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.department' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.department'
        db.alter_column(u'hackathon_profile', 'department', self.gf('django.db.models.fields.CharField')(max_length=64))

        # User chose to not deal with backwards NULL issues for 'UserProfile.photo_url'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.photo_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserProfile.photo_url'
        db.alter_column(u'hackathon_profile', 'photo_url', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'hackathon.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "u'hackathon_profile'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'cube': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'ext': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "u'subodinates'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['hackathon']