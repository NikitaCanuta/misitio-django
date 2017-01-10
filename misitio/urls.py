from django.conf.urls import url
from django.contrib import admin
from misitio.views import hola, fecha_actual, horas_adelante
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^hola/$',hola),
    url(r'^fecha/$',fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$',horas_adelante),
]
