from django.urls import path
from .views import *

urlpatterns = [
    path('',VideosListView.as_view(), name='videos-list'),
    path('mis_videos', VideosSubidos.as_view(), name='my-videos'),
    path('videos/<pk>', display_video, name='videos-detail'),
    path('no_download', error_descarga, name='iniciar_sesion'),
    path('contacto', contacto, name='contacto'),
]