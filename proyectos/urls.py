from django.urls import path
from .views import lista_proyectos, home

urlpatterns = [
    path('', lista_proyectos, name='lista_proyectos'),
    path('home/',home, name='home'),
]