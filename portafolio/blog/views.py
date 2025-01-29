from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})
    

def blog_detalle(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detalle.html', {'blog': blog})