# -*- coding: utf-8 -*-
from django.db import models
#Se importa los usuarios para usarlo en Producto
from django.contrib.auth.models import User

#Se crea el modelo de categoría
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

#Se crea el modelo para los productos
class Producto(models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, unique=True)
	categoria = models.ForeignKey(Categoria)
	descripcion = models.TextField()
	#Cambio hecho por South
	disponible = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre