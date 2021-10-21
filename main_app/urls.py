from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #route for fish index
    path('fishes/', views.fishes_index, name='index'),
    path('fishes/<int:fish_id>/', views.fishes_detail, name='detail'),
    # new route used to show a form and create a cat
    path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fishes_update'),
    path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fishes_delete'),
    path('fishes/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]

