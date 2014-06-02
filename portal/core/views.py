# coding: utf-8
from portal.core.models import Pagina
from portal.core.forms import SiteForm
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'core/portal.html')


def exemplo_form_admin(request):
    return render(request, 'core/exemplo_form_admin.html', {'form': SiteForm()})


def thumbnail(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    return render (request, 'core/thumbnail.html', {'pagina': pagina})