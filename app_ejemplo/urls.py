from django.urls import path
from . import views


urlpatterns = [
    path('ejemplo/<str:nombre>/', views.ejemplo, name='ejemplo')
]