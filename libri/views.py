from django.shortcuts import render
from .models import Libro

def lista_libri(request):
    lista_libri = Libro.objects.all()  # Recupera tutti i record del modello Libro
    return render(request, 'libri/lista.html', {'libri': libri})
