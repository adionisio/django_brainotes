# from django.forms import widgets
from django.forms import widgets
from rest_framework import serializers
from notas.models import Usuario
from notas.models import Nota

__author__ = 'braiNotes'

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model =  Usuario
        fields = ('id','nombre')

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Nota
        fields = ('id','usuario','fecha_Hora','titulo','cuerpo','recordatorio','color')
