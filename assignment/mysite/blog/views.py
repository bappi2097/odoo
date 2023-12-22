from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm
from django.views import View

def blogList(request):
    blogs = Blog.objects.all()
    return render(request, "blog_list.html", {'blogs': blogs})

def blogDetail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, "blog_detail.html", {'blog': blog})

class BlogCreateView(View):
    def get(self, request):
        form = BlogForm()
        return render(request, "blog_form.html", {'form': form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
        return render(request, "blog_form.html", {'form': form})

class BlogUpdateView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = BlogForm(instance=blog)
        return render(request, "blog_form.html", {'form': form})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
        return render(request, "blog_form.html", {'form': form})

class BlogDeleteView(View):
    success_url = reverse_lazy("blog-list")

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, "blog_confirm_delete.html", {'blog': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect(self.success_url)
    
