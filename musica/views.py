from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
import os


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
    lista=Videos.objects.all()
    return render(
        request,
        'index.html',
        context={'lista':lista},
    )

class VideosListView(generic.ListView):
    model = Videos


"""
def display_video(request,pk=None):
    if pk is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(Videos, pk)
        file_name = video_object.nombre
        # getting full url -
        video_url = settings.MEDIA_URL + file_name
        return render(request, "videos_detail.html", context={"url": video_url})
    except Videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")
        
def display_video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(videos, pk = vid)
    except videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.file_name
    #getting full url - 
    video_url = settings.MEDIA_URL+file_name

    return render(request, "video_template.html", {"url":video_url})

def display_video(request, pk):
    video_id=Videos.objects.get(pk=pk)
    return render(
      request,
      'musica/videos_detail.html',
      context={'video':video_id}
    )

def display_video(request,pk=None):
    if pk is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(Videos, pk = pk)
    except Videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.nombre
    #getting full url -
    video_url = settings.MEDIA_URL+file_name

    return render(request, "musica/videos_detail.html", {"url":video_url})

"""

def display_video(request,pk=None):
    if pk is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(Videos, pk = pk)
    except Videos.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.nombre
    #getting full url -
    video_url = settings.MEDIA_URL+file_name

    return render(request, "musica/videos_detail.html", {"video":video_object})


def download_videos(request, path):
    file_path= os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type="aplication/archivo_video")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise HttpResponse("No se puede descargar")

def error_descarga(request):
    return render(
        request,
        'musica/iniciar_sesion.html',
    )

def registro_usuario(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
