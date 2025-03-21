from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumne/', views.index1, name='alumne'),
    path('professor/', views.index2, name='professor'),
    path('alumne_detall/<int:alumno_id>/', views.alumne_detall, name='alumne_detall'),
    path('professor_detall/<int:profe_id>/', views.professor_detall, name='professor_detall'),
    path('alumne/form/', views.alumne_form_view, name='alumne_form'),
    path('professor/form/', views.professor_form_view, name='professor_form'),
]
