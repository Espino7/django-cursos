from django.contrib import admin
from .models import Curso

# Register your models here.

#Permite visualizar los campos automaticos
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'precio', 'disponibilidad', 'nivel')
    search_fields = ('titulo', 'nivel')
    date_hierarchy = 'created'
    list_filter = ('nivel','disponibilidad') 

admin.site.register(Curso, AdministrarModelo)
