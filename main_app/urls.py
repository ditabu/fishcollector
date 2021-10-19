from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #route for fish index
    path('fishes/', views.fishes_index, name='index'),
]