from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from proyectos.models import Proyecto
from blog.models import Blog


def home(request):
    return render(request, 'accounts/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirigir al dashboard después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirigir al dashboard después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    """
    Vista para el dashboard del usuario.
    Muestra los proyectos asociados al usuario actual.
    """
    # Filtra los proyectos del usuario actual
    proyectos = Proyecto.objects.filter(creado_por=request.user)
    blogs = Blog.objects.order_by('-fecha_de_publicacion')[:3]
    
    # Contexto para la plantilla
    context = {
        'proyectos': proyectos,
        'blogs': blogs,
    }
    return render(request, 'accounts/dashboard.html', context)