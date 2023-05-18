from django.shortcuts import render, redirect

from administracion.forms import CategoriaForm, CursoForm

from administracion.models import Categoria, Curso

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',
                  {'variable':variable})

"""
    CRUD Categorias
"""
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request,'administracion/categorias/nuevo.html',{'form':formulario})

def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(request,'administracion/categorias/editar.html',{'form':formulario})

def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    categoria.soft_delete()
    return redirect('categorias_index')

"""
    CRUD Cursos
"""
def cursos_index(request):
    #queryset
    cursos = Curso.objects.all()
    return render(request,'administracion/cursos/index.html',{'cursos':cursos})

def cursos_nuevo(request):
    if(request.method=='POST'):
        formulario = CursoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('cursos_index')
    else:
        formulario = CursoForm()
    return render(request,'administracion/cursos/nuevo.html',{'form':formulario})

def cursos_editar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CursoForm(request.POST,request.FILES, instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect('cursos_index')
    else:
        formulario = CursoForm(instance=curso)
    return render(request,'administracion/cursos/editar.html',{'form':formulario})

def cursos_eliminar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    curso.delete()
    return redirect('cursos_index')

"""
    IMPLEMENTACION DE CRUD DE CATEGORIA POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
"""
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name= 'administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']
    paginate_by = 6

class CategoriaCreateView(CreateView):
    model = Categoria
    # fields = ['nombre']
    form_class = CategoriaForm
    template_name = 'administracion/categorias/nuevo.html'
    success_url = reverse_lazy('categorias_index_view')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre']
    # form_class = CategoriaForm
    template_name = 'administracion/categorias/editar.html'
    success_url = reverse_lazy('categorias_index_view')

    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     obj = get_object_or_404(Categoria, pk=pk)
    #     return obj
    
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'administracion/categorias/eliminar.html'
    success_url = reverse_lazy('categorias_index_view')
    
    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     obj = get_object_or_404(Categoria, pk=pk)
    #     return obj
    
    #se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()  # Llamada al método soft_delete() del modelo
        return HttpResponseRedirect(self.get_success_url())