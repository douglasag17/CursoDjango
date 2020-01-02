from django.contrib import admin
from gestionPedidos.models import Cliente, Articulo, Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulo)
admin.site.register(Pedido)
