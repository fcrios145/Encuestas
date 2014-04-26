# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pregunta.catalogo'
        db.delete_column(u'inicio_pregunta', 'catalogo_id')

        # Adding M2M table for field preguntas on 'Catalogo'
        m2m_table_name = db.shorten_name(u'inicio_catalogo_preguntas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('catalogo', models.ForeignKey(orm[u'inicio.catalogo'], null=False)),
            ('pregunta', models.ForeignKey(orm[u'inicio.pregunta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['catalogo_id', 'pregunta_id'])


    def backwards(self, orm):
        # Adding field 'Pregunta.catalogo'
        db.add_column(u'inicio_pregunta', 'catalogo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['inicio.Catalogo']),
                      keep_default=False)

        # Removing M2M table for field preguntas on 'Catalogo'
        db.delete_table(db.shorten_name(u'inicio_catalogo_preguntas'))


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
        u'inicio.encuestacompleta': {
            'Meta': {'object_name': 'EncuestaCompleta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inicio.Persona']", 'unique': 'True'}),
            'preguntas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inicio.Pregunta']", 'symmetrical': 'False'}),
            'respuestas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inicio.Respuesta']", 'symmetrical': 'False'})
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