from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('mis_videos', VideosSubidos.as_view(), name='my-videos'),
    path('videos', VideosListView.as_view(), name='videos-list'), #El name es el nombre con el que referenciamos en el html
    path('videos/<pk>', display_video, name='videos-detail'),
    path('no_download', error_descarga, name='iniciar_sesion'),
    path('register', registro_usuario, name='register'),
]