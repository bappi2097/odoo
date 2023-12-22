from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

def authorList(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {'authors': authors})

def authorDetails(request,pk):
    author = Author.objects.filter(pk=pk).first()
    return render(request, "author_detail.html", {'author': author})


def authorCreate(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, "author_form.html", {'form': form})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
        return render(request, "author_form.html", {'form': form})

def authorUpdate(request, pk):
    if request.method == "GET":
        author = Author.objects.filter(id=pk).first()
        form = AuthorForm(instance=author)
        return render(request, "author_form.html", {'form': form})
    else:
        author = Author.objects.filter(id=pk).first()
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
        return render(request, "author_form.html", {'form': form})

def authorDelete(request, pk):
    if request.method == "GET":
        author = Author.objects.filter(id=pk).first()
        return render(request, "author_confirm_delete.html", {'author': author})
    else:
        author = Author.objects.filter(id=pk).first()
        author.delete()
        return redirect('author-list')
    
