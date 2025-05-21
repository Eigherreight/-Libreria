from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libri, name='lista_libri'),
    path('<int:id>/', views.dettaglio_libro, name='dettaglio_libro'),
]
