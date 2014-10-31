# -*- coding: utf-8 -*-
import functools
from portal.core.models import ContadorVisitas


def contar_acesso(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        contador, contador_criado = ContadorVisitas.objects.get_or_create(url=request.path)
        contador.contagem += 1
        contador.save()

        return method(request, *args, **kwargs)

    return wrapper