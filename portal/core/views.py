# coding: utf-8
from collections import OrderedDict
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.shortcuts import render, redirect
from django.http import HttpResponse  # httresponse para usar com json
from django.http.response import Http404
import json  # json para usar no select com ajax
from haystack.views import SearchView
from pure_pagination import Paginator, PageNotAnInteger

from portal.core.models import Menu
from portal.core.models import Destino
from portal.core.models import Selecao, TipoSelecao
from portal.conteudo.models import Noticia
from portal.conteudo.models import Evento
from portal.conteudo.models import Video
from portal.conteudo.models import Galeria
from portal.banner.models import Banner
from portal.cursos.models import Curso


def home(request):
    contexto = dict()
    try:
        site = Site.objects.get(domain=request.get_host())

        if site.sitedetalhe.destino.tipo == Destino.redirect():
            return redirect(site.sitedetalhe.destino.caminho)

        elif site.sitedetalhe.destino.tipo == Destino.portal():
            noticias_detaque = sorted(Noticia.publicados.filter(destaque=True, sites__id__exact=site.id)[:5],
                                      key=lambda o: o.prioridade_destaque)
            mais_noticias = Noticia.publicados.filter(sites__id__exact=site.id).exclude(
                id__in=[obj.id for obj in noticias_detaque])[:10]
            eventos = Evento.publicados.filter(sites__id__exact=site.id)[:3]
            videos = Video.publicados.filter(sites__id__exact=site.id)[:1]
            galerias = Galeria.publicados.filter(sites__id__exact=site.id)[:3]

            banners_destaque = Banner.destaque.filter(sites__id__exact=site.id)[:4]
            banners_linkdeacesso = Banner.linkdeacesso.filter(sites__id__exact=site.id)[:5]
            banners_governamental = Banner.governamental.filter(sites__id__exact=site.id)
            formacao = Curso.objects.select_related('Formacao').values('formacao__id', 'formacao__nome').distinct()
            contexto = {
                'noticias_destaque': noticias_detaque,
                'mais_noticias': mais_noticias,
                'eventos': eventos,
                'banners_destaque': banners_destaque,
                'banners_linkdeacesso': banners_linkdeacesso,
                'banners_governamental': banners_governamental,
                'videos': videos,
                'galerias': galerias,
                'formacao': formacao,
            }

        elif site.sitedetalhe.destino.tipo == Destino.portal_secundario():
            noticias_detaque = sorted(Noticia.publicados.filter(destaque=True, sites__id__exact=site.id)[:5],
                                      key=lambda o: o.prioridade_destaque)
            mais_noticias = Noticia.publicados.filter(sites__id__exact=site.id).exclude(
                id__in=[obj.id for obj in noticias_detaque])[:6]
            eventos = Evento.publicados.filter(sites__id__exact=site.id)[:3]
            videos = Video.publicados.filter(sites__id__exact=site.id)[:1]
            galerias = Galeria.publicados.filter(sites__id__exact=site.id)[:3]

            banners_destaque = Banner.destaque.filter(sites__id__exact=site.id)[:4]
            banners_linkdeacesso = Banner.linkdeacesso.filter(sites__id__exact=site.id)[:5]
            banners_governamental = Banner.governamental.filter(sites__id__exact=site.id)
            formacao = Curso.objects.select_related('Formacao').values('formacao__id', 'formacao__nome').distinct()
            contexto = {
                'noticias_destaque': noticias_detaque,
                'mais_noticias': mais_noticias,
                'eventos': eventos,
                'banners_destaque': banners_destaque,
                'banners_linkdeacesso': banners_linkdeacesso,
                'banners_governamental': banners_governamental,
                'videos': videos,
                'galerias': galerias,
                'formacao': formacao,
            }

        elif site.sitedetalhe.destino.tipo == Destino.blog_slider():
            try:
                page = request.GET.get('page', 1)

            except PageNotAnInteger:
                page = 1

            noticias_detaque = sorted(Noticia.publicados.filter(destaque=True, sites__id__exact=site.id)[:5],
                                      key=lambda o: o.prioridade_destaque)
            objects = Noticia.publicados.filter(sites__id__exact=site.id).exclude(
                id__in=[obj.id for obj in noticias_detaque])
            paginator = Paginator(objects, request=request, per_page=5)
            mais_noticias = paginator.page(page)

            videos = Video.publicados.filter(sites__id__exact=site.id)[:1]
            galerias = Galeria.publicados.filter(sites__id__exact=site.id)[:3]
            banners = Banner.publicados.filter(sites__id__exact=site.id).order_by('tipo')
            contexto = {
                'noticias_destaque': noticias_detaque,
                'mais_noticias': mais_noticias,
                'videos': videos,
                'galerias': galerias,
                'banners': banners,
            }

        elif site.sitedetalhe.destino.tipo == Destino.blog():
            try:
                page = request.GET.get('page', 1)

            except PageNotAnInteger:
                page = 1

            objects = Noticia.publicados.filter(sites__id__exact=site.id)
            paginator = Paginator(objects, request=request, per_page=5)
            noticias = paginator.page(page)

            videos = Video.publicados.filter(sites__id__exact=site.id)[:1]
            galerias = Galeria.publicados.filter(sites__id__exact=site.id)[:3]
            banners = Banner.publicados.filter(sites__id__exact=site.id).order_by('tipo')
            contexto = {
                'noticias': noticias,
                'videos': videos,
                'galerias': galerias,
                'banners': banners,
            }

        elif site.sitedetalhe.destino.tipo == Destino.banners():
            banners = Banner.publicados.filter(sites__id__exact=site.id)

            contexto = {
                'banners': banners,
            }

    except (Site.DoesNotExist, Noticia.DoesNotExist, Evento.DoesNotExist,
            Banner.DoesNotExist, Video.DoesNotExist,
            Galeria.DoesNotExist, Curso.DoesNotExist):
        raise Http404

    return render(request, site.sitedetalhe.destino.caminho, contexto)


def selecao(request):
    lista = Selecao.objects.all()
    menu = TipoSelecao.objects.all()

    titulo = 0
    tipo = request.GET.get('tipo')
    status = request.GET.get('status')
    ano = request.GET.get('ano')

    if tipo:
        lista = lista.filter(tipo=tipo)
        titulo = menu.get(id=tipo)
        tipo = 'tipo=' + tipo + '&'
    else:
        tipo = ''

    if status:
        lista = lista.filter(status=status)
        status = 'status=' + status + '&'
    else:
        status = ''

    if ano:
        lista = lista.filter(data_abertura_edital__year=ano)
        ano = 'ano=' + ano
    else:
        ano = ''

    return render(request, 'core/selecao_lista.html', {
        'lista': lista,
        'ano': ano,
        'status': status,
        'tipo': tipo,
        'nodes': menu,
        'titulo': titulo
    })


def json_campi(request, formacao_id):
    campi = Curso.objects.select_related('Campus').filter(
        formacao=formacao_id).values_list('campus__id', 'campus__nome').distinct()
    dados = dict(campi)
    return HttpResponse(json.dumps(dados), content_type="application/json")


def json_cursos(request, formacao_id, campus_id):
    dados = dict(Curso.objects.select_related('GrupoCursos').filter(
        formacao=formacao_id, campus=campus_id).values_list('grupo__id', 'grupo__nome').distinct())
    return HttpResponse(json.dumps(dados), content_type="application/json")


@login_required
def admin_site_menu(request, site_id):
    try:
        site = Site.objects.get(id=site_id)
    except Site.DoesNotExist:
        raise Http404
    menus = Menu.objects.filter(site=site)

    return HttpResponse(json.dumps(serialize_menus(menus)), mimetype="application/json")


def serialize_menus(queryset):
    lista = []
    for menu in queryset:
        d = OrderedDict()
        d["ordem"] = menu.ordem
        d["id"] = menu.id
        d["titulo"] = '---' * menu.get_level() + ' ' + menu.titulo
        lista.append(d)
    return lista


class SearchViewSites(SearchView):
    # sobrescrita do metodo para filtar pelo dominio da requisicao
    def get_results(self):
        results = self.searchqueryset.filter(text__startswith=self.query)

        search_models = []

        if self.form.is_valid():
            for model in self.form.cleaned_data['models']:
                search_models.append(models.get_model(*model.split('.')))

            results = results.models(*search_models)

        results = results.filter(text__contains=self.request.get_host())

        return results

    def build_page(self):
        try:
            page = self.request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1

        page = int(page)
        paginator = Paginator(self.results, request=self.request, per_page=25)
        page_results = paginator.page(page)

        return paginator, page_results