from django import forms
from .models import Curso, Actividad

class CursosForm(forms.ModelForm):
    disponibilidad = forms.BooleanField(required=False)

    class Meta:
        model = Curso
        exclude = ['created', 'updated']

class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ['created', ]