from django.contrib import admin
from .models import Curso
from .models import Actividad

# Register your models here.

#Permite visualizar los campos automaticos
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'precio', 'disponibilidad', 'nivel')
    search_fields = ('titulo', 'nivel')
    date_hierarchy = 'created'
    list_filter = ('nivel','disponibilidad') 

admin.site.register(Curso, AdministrarModelo)

class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Actividad, AdministrarActividad)