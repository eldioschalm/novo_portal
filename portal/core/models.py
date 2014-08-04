# -*- coding: utf-8 -*-
from django.db import models
from filer.server.backends import default
from mptt.models import MPTTModel, TreeForeignKey

class Campus(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='pai', verbose_name='Nivel 1')
    sigla = models.CharField(max_length=3, verbose_name=u'Sigla do Campus')
    nome = models.CharField(max_length=50, verbose_name=u'Nome do Campus')
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = u'Campus'
        verbose_name_plural = u'Campi'

    def __unicode__(self):
        return self.nome


class Menu(MPTTModel):
    class Meta:
        ordering = ('ordem',)

    class MPTTMeta:
        order_insertion_by = ['ordem']

    parent = TreeForeignKey('self', null=True, blank=True, related_name='pai', verbose_name='Nivel 1')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    url = models.CharField(max_length=250, blank=True,)
    ordem = models.IntegerField(default=9999, blank=True, verbose_name=u'Ordem do Menu',)

    def __unicode__(self):
        return self.titulo

    def menu_raiz(self):
        if self.parent == None:
            return ""
        return self.parent


class TipoSelecao(MPTTModel):
    class Meta:
        ordering = ('titulo',)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='pai', verbose_name='Tipo pai')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.titulo


class Selecao(models.Model):

    # TIPO_BASE = (
    #     ('Vestibulares e Seleção',(
    #         ('VEST',u'Vestibulares'),
    #         ('SISU',u'SISU'),
    #         ('STEC',u'SISUTEC'),
    #         ('EXSE',u'Exames de Seleção'),
    #         ('PRSE',u'Processo Seletivo'),
    #         ('TREX',u'Transferência Externa')
    #         )
    #     ),
    #     ('Concursos Publicos',(
    #         ('DOCE',u'Docentes'),
    #         ('TEAD',u'Técnicos-administrativos'),
    #         )
    #     ),
    #     ('Processos Seletivos',(
    #         ('PRTE',u'Professores substitutos e/ou temporários'),
    #         ('PEAD',u'Processos Seletivos - EAD'),
    #         ('PPRO',u'Processsos Seletivos - PRONATEC'), ,
    #         ('ROID',u'Remoção Interna - Docentes'),
    #         ('ROIT',u'Remoção Interna - TAEs')
    #         )
    #     )
    # )

    STATUS = (
        ('ABT','Aberto'),
        ('AND','Em Andamento'),
        ('FNZ','Finalizado')
    )

    class Meta:
        ordering = ('titulo','status','data_abertura_edital')

    tipo = TreeForeignKey('TipoSelecao')
    titulo = models.CharField(max_length=100)
    url = models.CharField(max_length=250,)
    status = models.CharField(max_length=3, choices=STATUS)
    data_abertura_edital = models.DateTimeField(verbose_name=u'Data de Abertura do Edital')
    data_abertura_inscricoes = models.DateTimeField(verbose_name=u'Data de Abertura de Inscrições')
    data_encerramento_inscricoes = models.DateTimeField(verbose_name=u'Data de Fechamento das Incrições')
    data_publicacao = models.DateTimeField(verbose_name=u'Data de publicação')

    def __unicode__(self):
        return self.titulo
