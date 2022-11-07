from django.urls import path

from . import views

# dominio/recipes/home
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
