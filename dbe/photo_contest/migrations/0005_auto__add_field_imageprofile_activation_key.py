# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ImageProfile.activation_key'
        db.add_column(u'photo_contest_imageprofile', 'activation_key', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ImageProfile.activation_key'
        db.delete_column(u'photo_contest_imageprofile', 'activation_key')


    models = {
        u'photo_contest.imageprofile': {
            'Meta': {'ordering': "['created']", 'object_name': 'ImageProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'banned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birthday': ('django.db.models.fields.DateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'confirm_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'personal_info': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['photo_contest.Promotion']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'photo_contest.promotion': {
            'Meta': {'object_name': 'Promotion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'})
        }
    }

    complete_apps = ['photo_contest']
