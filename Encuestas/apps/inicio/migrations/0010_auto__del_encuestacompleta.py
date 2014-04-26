# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EncuestaCompleta'
        db.delete_table(u'inicio_encuestacompleta')

        # Removing M2M table for field preguntas on 'EncuestaCompleta'
        db.delete_table(db.shorten_name(u'inicio_encuestacompleta_preguntas'))

        # Removing M2M table for field respuestas on 'EncuestaCompleta'
        db.delete_table(db.shorten_name(u'inicio_encuestacompleta_respuestas'))


    def backwards(self, orm):
        # Adding model 'EncuestaCompleta'
        db.create_table(u'inicio_encuestacompleta', (
            ('persona', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inicio.Persona'], unique=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'inicio', ['EncuestaCompleta'])

        # Adding M2M table for field preguntas on 'EncuestaCompleta'
        m2m_table_name = db.shorten_name(u'inicio_encuestacompleta_preguntas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encuestacompleta', models.ForeignKey(orm[u'inicio.encuestacompleta'], null=False)),
            ('pregunta', models.ForeignKey(orm[u'inicio.pregunta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encuestacompleta_id', 'pregunta_id'])

        # Adding M2M table for field respuestas on 'EncuestaCompleta'
        m2m_table_name = db.shorten_name(u'inicio_encuestacompleta_respuestas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encuestacompleta', models.ForeignKey(orm[u'inicio.encuestacompleta'], null=False)),
            ('respuesta', models.ForeignKey(orm[u'inicio.respuesta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encuestacompleta_id', 'respuesta_id'])


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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'preguntas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inicio.Pregunta']", 'symmetrical': 'False'})
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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'respuestas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inicio.Respuesta']", 'symmetrical': 'False'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'inicio.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['inicio']