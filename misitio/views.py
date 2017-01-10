from django.http import HttpResponse, Http404
import datetime

def hola(request):
    return HttpResponse("Hola Mundo")


def fecha_actual(request):
    ahora = datetime.datetime.now()
    html ="<html><body><h1>Fecha:</h1><h3>%s</h3></body></html>" %ahora
    return HttpResponse(html)

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt= datetime.datetime.now() + datetime.timedelta(hours=horas)
    html ="<html><body><h1>En %s horas(s), seran</h1><h3>%s</h3></body></html>" %(horas, dt)
    return HttpResponse(html)
