# error/views.py
from django.shortcuts import render

# Vista para el error 404
def error_404(request, exception):
    return render(request, 'error/404.html', status=404)

