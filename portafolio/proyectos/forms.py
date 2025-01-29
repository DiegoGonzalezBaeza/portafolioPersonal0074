from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_de_inicio', 'fecha_de_finalizacion', 'estado_actual']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del proyecto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del proyecto'}),
            'fecha_de_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_de_finalizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_actual': forms.Select(attrs={'class': 'form-control'}),
        }