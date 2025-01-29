from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto_view, name='contacto'),  # Página del formulario
    path('gracias/', views.gracias_view, name='gracias'),  # Página de agradecimiento
]