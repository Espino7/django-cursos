from django.shortcuts import render, HttpResponse

# Create your views here.

def principal(request):
    return render(request, "contenido/principal.html")

def notFound(request):
    return render(request,"contenido/404.html")

def contacto(request):
    return render(request, "contenido/contacto.html")

def cursos(request):
    return render(request, "contenido/cursos.html")