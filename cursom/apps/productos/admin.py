from django.contrib import admin
from cursom.apps.productos.models import Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)