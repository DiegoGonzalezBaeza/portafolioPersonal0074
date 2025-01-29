from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm
from django.shortcuts import render, redirect

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar el formulario
            form.save()

            # Redirigir a la página de gracias
            return redirect('gracias')  # Redirige a la vista 'gracias'
    else:
        form = ContactoForm()

    return render(request, 'contacto/contacto.html', {'form': form})

def gracias_view(request):
    return render(request, 'contacto/gracias.html')