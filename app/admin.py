from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["producto_nombre","producto_precio","producto_cantidad","producto_marca"]
    list_editable = ["producto_precio"]
    search_fields = ["producto_nombre","producto_marca"]
    list_filter = ["producto_marca","producto_nombre"]
    list_per_page = 25

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Categoria)