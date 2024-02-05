from django.urls import path
from prueba.views import pruebaEndpoint, nuevoEndpoint

urlpatterns = [
    path("hola", pruebaEndpoint),
    path("nuevo", nuevoEndpoint)
]