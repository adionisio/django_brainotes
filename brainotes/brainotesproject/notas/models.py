# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=30)
	def __str__(self):
		return '%s' % (self.nombre)

class Nota(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='nota')
	fecha_Hora = models.DateTimeField()
	titulo = models.CharField(max_length=50)
	cuerpo = models.CharField(max_length=500)
	recordatorio = models.IntegerField(default=0)
	color = models.CharField(max_length=15)
	
