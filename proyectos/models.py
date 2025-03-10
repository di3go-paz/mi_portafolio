from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    url = models.URLField(blank=True)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
