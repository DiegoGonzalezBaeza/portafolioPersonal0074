from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.fecha_de_publicacion}'