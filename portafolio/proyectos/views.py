from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from .forms import ProyectoForm

# Create your views here.
@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(creado_por=request.user)
    return render(request, 'proyectos/proyectos.html', {'proyectos': proyectos})

@login_required
def proyecto_detalle(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'proyectos/proyecto_detalle.html', {'proyecto': proyecto})

@login_required
def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.creado_por = request.user
            proyecto.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/proyectos_form.html', {'form': form})

@login_required
def proyecto_update(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, creado_por=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/proyectos_form.html', {'form': form})

@login_required
def proyecto_delete(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, creado_por=request.user)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyectos')
    return render(request, 'proyectos/proyectos_confirm_delete.html', {'proyecto': proyecto})