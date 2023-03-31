from django.shortcuts import render, HttpResponse

# Create your views here.

def posts(request):
    return HttpResponse('<h1>paginas de publicaciones</h1>')

def post(request, id):
    return HttpResponse('<h1>pagina de blog</h1>')
    