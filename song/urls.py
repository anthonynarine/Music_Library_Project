from django.urls import path
from . import views

urlpatterns = [
    path("app_home", views.song_list),    #http://127.0.0.1:8000/api/song/app_home
]