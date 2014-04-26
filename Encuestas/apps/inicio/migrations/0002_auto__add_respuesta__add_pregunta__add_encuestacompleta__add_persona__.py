# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Respuesta'
        db.create_table(u'inicio_respuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inicio.Pregunta'])),
        ))
        db.send_create_signal(u'inicio', ['Respuesta'])

        # Adding model 'Pregunta'
        db.create_table(u'inicio_pregunta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('catalogo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inicio.Catalogo'])),
        ))
        db.send_create_signal(u'inicio', ['Pregunta'])

        # Adding model 'EncuestaCompleta'
        db.create_table(u'inicio_encuestacompleta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inicio.Persona'], unique=True)),
        ))
        db.send_create_signal(u'inicio', ['EncuestaCompleta'])

        # Adding model 'Persona'
        db.create_table(u'inicio_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inicio.Carrera'])),
            ('genero', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inicio', ['Persona'])

        # Adding model 'Catalogo'
        db.create_table(u'inicio_catalogo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'inicio', ['Catalogo'])


    def backwards(self, orm):
        # Deleting model 'Respuesta'
        db.delete_table(u'inicio_respuesta')

        # Deleting model 'Pregunta'
        db.delete_table(u'inicio_pregunta')

        # Deleting model 'EncuestaCompleta'
        db.delete_table(u'inicio_encuestacompleta')

        # Deleting model 'Persona'
        db.delete_table(u'inicio_persona')

        # Deleting model 'Catalogo'
        db.delete_table(u'inicio_catalogo')


    models = {
        u'inicio.carrera': {
            'Meta': {'object_name': 'Carrera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'inicio.catalogo': {
            'Meta': {'object_name': 'Catalogo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'inicio.encuestacompleta': {
            'Meta': {'object_name': 'EncuestaCompleta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inicio.Persona']", 'unique': 'True'})
        },
        u'inicio.persona': {
            'Meta': {'object_name': 'Persona'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inicio.Carrera']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'genero': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inicio.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'catalogo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inicio.Catalogo']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'inicio.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inicio.Pregunta']"}),
            'texto': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['inicio']