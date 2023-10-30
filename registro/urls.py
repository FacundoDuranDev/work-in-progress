from django.urls import path
from . import views


urlpatterns = [
    path('añadir/<str:nombre>/', views.añadir, name='añadir'),
    path("mirar_registros/", views.mirar_registros, name="mirar_registros"),
    path("eliminar/<str:nombre>/", views.eliminar, name="eliminar")
]