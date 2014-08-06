# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campus'
        db.create_table(u'cursos_campus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'cursos', ['Campus'])

        # Adding model 'Formacao'
        db.create_table(u'cursos_formacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cursos', ['Formacao'])

        # Adding model 'Grupo_Cursos'
        db.create_table(u'cursos_grupo_cursos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cursos', ['Grupo_Cursos'])

        # Adding model 'Curso'
        db.create_table(u'cursos_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('formacao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Formacao'])),
            ('campus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Campus'])),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Grupo_Cursos'])),
        ))
        db.send_create_signal(u'cursos', ['Curso'])


    def backwards(self, orm):
        # Deleting model 'Campus'
        db.delete_table(u'cursos_campus')

        # Deleting model 'Formacao'
        db.delete_table(u'cursos_formacao')

        # Deleting model 'Grupo_Cursos'
        db.delete_table(u'cursos_grupo_cursos')

        # Deleting model 'Curso'
        db.delete_table(u'cursos_curso')


    models = {
        u'cursos.campus': {
            'Meta': {'object_name': 'Campus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cursos.curso': {
            'Meta': {'object_name': 'Curso'},
            'campus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Campus']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'formacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Formacao']"}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Grupo_Cursos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cursos.formacao': {
            'Meta': {'object_name': 'Formacao'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cursos.grupo_cursos': {
            'Meta': {'object_name': 'Grupo_Cursos'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['cursos']