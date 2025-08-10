"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
'Importamos nuestras vistas desde la carpeta contenido'
from contenido import views
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('404/', views.notFound, name="404"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursos/', views.cursos, name="Cursos"),

    # Crud
    path('formCursos/', views_cursos.registrarCurso, name='registrar_curso'),
    path('listaCurso/', views_cursos.listaCursos, name='lista_cursos'),
    path('cursos/<int:id>', views_cursos.consultarCursoIndividual, name='consultar_curso'),
    path('formEditarCurso/<int:id>', views_cursos.editarCurso, name='editar_curso'),
    path('eliminarCurso/<int:id>', views_cursos.eliminarCurso, name='eliminar_curso'),
]

# Agrega rutas para archivos media solo si estás en modo DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)