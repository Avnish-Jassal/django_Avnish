from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('CrearCuenta/', views.CrearCuenta_view, name='CrearCuenta'),
]