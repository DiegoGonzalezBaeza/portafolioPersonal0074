from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.lista_blogs, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detalle, name='blog_detalle'),
]
