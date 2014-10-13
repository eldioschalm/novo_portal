# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import CharField
from django.forms import TextInput
import reversion

from portal.cursos.models import Curso
from portal.cursos.models import Formacao
from portal.cursos.models import GrupoCursos
from portal.cursos.models import AnexoCurso
from portal.cursos.forms import CursoForm


class FormacaoAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    pass

admin.site.register(Formacao, FormacaoAdmin)


class AnexoCursoInLine(admin.StackedInline):

    model = AnexoCurso
    extra = 1

    formfield_overrides = {
        CharField: {'widget': TextInput(attrs={'size': '85'})},
        # from django.forms import Textarea
        # TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


class CursoAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    form = CursoForm

    inlines = (AnexoCursoInLine, )

admin.site.register(Curso, CursoAdmin)


class GrupoCursosAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    pass

admin.site.register(GrupoCursos, GrupoCursosAdmin)