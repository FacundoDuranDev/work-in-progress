from django.shortcuts import render

# Create your views here.
# request => response
# request handler
# action
variable_global = []
def ejemplo(request, nombre):
    if nombre not in variable_global:
        variable_global.append(nombre)
    return render(request, "ejemplo.html", {"variable": nombre, "personas": variable_global})