from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Miusuario, UserAdmin)
#admin.site.register(Videos)

# Definimos la clase admin
class SubgeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(Subgenero, SubgeneroAdmin)
list_display = ('nombre')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'subgenero', 'año', 'usuario', 'archivo_video')
    list_filter = ('nombre', 'autor', 'año')
