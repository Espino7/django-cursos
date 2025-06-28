from django.db import models

# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=200) # 1,- Texto corto
    descripcion = models.TextField(verbose_name="Descripción") # 2.- Texto largo
    imagen = models.ImageField(null=True, upload_to="cursos", verbose_name="Imagen") # Default - Imagen
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Default - Creación
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización") # Extra 
    precio = models.DecimalField(max_digits=6, decimal_places=2) # 3.- Décimal
    disponibilidad = models.BooleanField(default=True) # 4.- Booleano

    # Declarar la lista de opciones
    NIVELES = [
        ('BAS','Básico'),
        ('INT','Intermedio'),
        ('ADV','Avanzado'),
    ]
    nivel = models.CharField(max_length=3, choices=NIVELES, default='BAS') # 5.- Lista

    class Meta:
        # Cambia el nombre de la lista
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        # Si se le pone un - pone las más actuales primero.
        ordering = ["created"]
    def __str__(self):
        return self.titulo