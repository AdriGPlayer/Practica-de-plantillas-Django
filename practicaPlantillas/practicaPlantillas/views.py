from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    contexto = {
        'titulo': 'Juanjo Ruiz - Fotografo'
    }
    return render(request, 'index.html', contexto)

def portafolio(request):
    return render(request, 'portafolio.html', {
        'titulo': 'Portafolio'
    })
    