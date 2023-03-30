from django.http import HttpResponse

def hola(request):
    """ print(request) """
    return HttpResponse("Hola mundo desde Django")
