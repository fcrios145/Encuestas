# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Respuesta.pregunta'
        db.add_column(u'inicio_respuesta', 'pregunta',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['inicio.Pregunta']),
                      keep_default=False)

        # Removing M2M table for field pregunta on 'Respuesta'
        db.delete_table(db.shorten_name(u'inicio_respuesta_pregunta'))


    def backwards(self, orm):
        # Deleting field 'Respuesta.pregunta'
        db.delete_column(u'inicio_respuesta', 'pregunta_id')

        # Adding M2M table for field pregunta on 'Respuesta'
        m2m_table_name = db.shorten_name(u'inicio_respuesta_pregunta')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('respuesta', models.ForeignKey(orm[u'inicio.respuesta'], null=False)),
            ('pregunta', models.ForeignKey(orm[u'inicio.pregunta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['respuesta_id', 'pregunta_id'])


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