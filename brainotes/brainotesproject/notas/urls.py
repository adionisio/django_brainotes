__author__ = 'braiNotes'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notas import views

"""
    Adding my braiNotes Routes
"""
urlpatterns = [
#   url(r'^$', views.api_root),
    url(r'^notas/$', views.notas_list),
    url(r'^notas/(?P<pk>[0-9]+)/$', views.nota_detail),
    url(r'^usuarios/$', views.usuarios_list),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.usuario_detail)
#    url(r'^usuarios/(?P<pk>[0-9]+)/notas/', views.usuario_notas)
#    url(r'^contacts/$', views.contact_list),
#    url(r'^contacts/(?P<pk>[0-9]+)/$', views.contact_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
