from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la pagina principal de nuestro servidor")