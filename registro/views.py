from django.shortcuts import render

# Create your views here.

# request => response

def añadir(request, nombre):
    with open("registro.txt", "a") as archivo:
        archivo.write(nombre + ",")
        archivo.close()
        return render(request,"añadir.html", {"nombre": nombre})

def eliminar(request, nombre):
    with open("registro.txt", "r") as archivo:
        string_ = archivo.read()
        archivo.close()
    with open("registro.txt", "w") as archivo:
        string_ = string_.replace(nombre + ",", "")
        archivo.write(string_)
        archivo.close()
    return render(request,"eliminar.html", {"nombre": nombre})

def mirar_registros(request):
    with open("registro.txt", "r") as archivo:
        string_completo = archivo.read()
        lista_nombres = string_completo.split(",")
        archivo.close()
        return render(request,"mirar_registros.html", {"lista_nombres": lista_nombres})