from django.urls import path
from . import views
from django.urls import path
urlpatterns = [
    path('index/', views.index, name='home'),
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('quiz/', views.quiz, name='quiz'),
    path('transcribe_audio/', views.transcribe_audio, name="transcribe_audio"),
    path('index/', views.index, name="index"),
    path('quiz/', views.quiz, name='quiz'),
    path('transcribe/', views.transcribe_audio, name='transcribe_audio'),
    path('view_transcripts/', views.view_transcripts, name='view_transcripts'),
    path('quiz/', views.quiz, name='quiz'),
]
