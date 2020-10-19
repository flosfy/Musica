from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Miusuario(AbstractUser):
    usuario_id=models.AutoField(primary_key=True)


class Subgenero(models.Model):
    subgenero_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('subgenero-detail', args=[str(self.subgenero_id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return self.nombre


class Videos(models.Model):
    video_id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    autor=models.CharField(max_length=200)
    subgenero=models.ForeignKey(Subgenero, on_delete=models.DO_NOTHING, default=None)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.CASCADE, default=None)
    año=models.CharField(max_length=50, null=True, blank=True, default=None)
    archivo_video= models.FileField(upload_to='videos/%y', null=True, verbose_name="")

    def __str__(self):
        return self.nombre
        #return self.nombre +":" +str(self.archivo_video)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Videos
        """
        return reverse('videos-detail', args=[str(self.video_id)])




