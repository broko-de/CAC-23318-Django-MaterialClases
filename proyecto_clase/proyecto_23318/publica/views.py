from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f"""<h1>Proyecto Django - Codo a Codo🦄</h1>""")
    
def quienes_somos(request):
    return HttpResponse(f"""<h1>Quienes somos 🙇‍♂️</h1>""")
    
def saludar(request,nombre):
    if(request.method=='GET'):
        return HttpResponse(f"""
            <h1>ENTRE POR GET - {nombre}</h1>
        """)
    else:
        return HttpResponse(f"""
            <h1>Hola Django - {nombre}</h1>
        """)