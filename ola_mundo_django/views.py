from django.http import HttpResponse
from django.shortcuts import render

def ola_mundo(request):
    # Responde um texto dentro do HTTP
    #return HttpResponse("Ola mundo")

    # Responde um arquivo HTML gerado pelo Django
    # texto = "'Olá Mundo!!!!! \n Olá Mundo!!!!!'"
    return render(request, "ola_mundo.html")

