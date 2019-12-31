from django.contrib import admin

# Register your models here.

from .models import Clientes, Articulos, Pedidos

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)