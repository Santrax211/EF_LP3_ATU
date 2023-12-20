from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def productos(request):
    return render(request, 'productos.html')

def crear_productos(request):
    return render(request, 'crear_productos.html')

def crear_cursos(request):
    return render(request, 'crear_cursos.html')

