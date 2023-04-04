from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    if(request.GET.get('param')):
        param_uno = request.GET.get('param')
    else:
        param_uno='defecto'
    param_dos = request.GET.get('param2')
    return render(request,'publica/index.html',{'param_uno':param_uno})
    # return HttpResponse(f"""
    #     <h1>Proyecto Django - Codo a Codo🦄</h1>
    #     <p>Param: {param_uno}</p>
    #     <p>Param 2: {param_dos}</p>
    #     """)
    
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
    
def ver_proyectos(request,anio,mes=1):    
    return HttpResponse(f"""
            <h1>Proyectos del  {mes}/{anio}</h1>
        """)

def ver_proyectos_2023_04(request):    
    return HttpResponse(f"""
            <h1>Proyectos del mes de Abril 2023</h1>
        """)