from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Blog

# def create_blog(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         slug = slugify(title)
#         blog = Blog(title=title, content=content, slug=slug)
#         blog.save()
#         return redirect('blog_detail', slug=blog.slug)
#     return render(request, 'blog_list.html')



def blog_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        slug = slugify(title)
        blog = Blog(title=title, content=content, slug=slug)
        blog.save()
        return redirect('blog_detail', slug=blog.slug)
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
