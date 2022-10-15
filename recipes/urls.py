from django.urls import path

from recipes.views import contato, home, sobre

# dominio/recipes/home
urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato', contato),
]