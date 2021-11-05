from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def historia(request):
    return render(request, 'core/historia.html')

def menu(request):
    return render(request, 'core/menu.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def blog(request):
    return render(request, 'core/blog.html')

