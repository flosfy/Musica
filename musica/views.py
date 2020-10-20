from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
import os
from django.core.mail import send_mail


class VideosSubidos(LoginRequiredMixin, generic.ListView):
    """
    Vista basada en la clase Generic que muestra los videos subidos por el usuario actual.
    """
    model = Videos
    template_name = 'musica/videos_del_usuario.html'
    paginate_by = 1

    def get_queryset(self):
        return Videos.objects.filter(usuario=self.request.user).order_by('nombre')


def index(request):
    lista = Videos.objects.all()
    return render(
        request,
        'index.html',
        context={'lista': lista},
    )


class VideosListView(generic.ListView):
    model = Videos



def display_video(request, pk=None):
    if pk is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(Videos, pk=pk)
    except Videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.nombre
    # getting full url -
    video_url = settings.MEDIA_URL + file_name

    return render(request, "musica/videos_detail.html", {"video": video_object})


def download_videos(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="aplication/archivo_video")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise HttpResponse("No se puede descargar")


def error_descarga(request):
    return render(
        request,
        'musica/iniciar_sesion.html',
    )


def contacto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        pais = request.POST['pais']
        ciudad = request.POST['ciudad']
        codigo_postal = request.POST['codigo-postal']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']

        send_mail(
            nombre,
            mensaje,
            correo,
            ['flosferri135@gmail.com']  # Este es el correo al que va a llegar el formulario de contacto
        )
        return render(request, 'musica/contacto.html', {'nombre': nombre})
    else:
        return render(request, 'musica/contacto.html', {})
