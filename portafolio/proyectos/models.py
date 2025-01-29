from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):

    ESTADOS = [
        ('En progreso', 'En progreso'),
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_de_inicio = models.DateField()
    fecha_de_finalizacion = models.DateField()
    estado_actual = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_proyectos', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} - {self.fecha_de_inicio} - {self.fecha_de_finalizacion} - {self.creado_por}'
    