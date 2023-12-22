from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Entry
from .forms import EntryForm

class EntryListView(View):
    template_name = "entry_list.html"

    def get(self, request):
        entries = Entry.objects.all()
        return render(request, self.template_name, {'entries': entries})

class EntryDetailView(View):
    template_name = "entry_detail.html"

    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        return render(request, self.template_name, {'entry': entry})

class EntryCreateView(View):
    template_name = "entry_form.html"

    def get(self, request):
        form = EntryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry-list')
        return render(request, self.template_name, {'form': form})

class EntryUpdateView(View):
    template_name = "entry_form.html"

    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        form = EntryForm(instance=entry)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry-list')
        return render(request, self.template_name, {'form': form})

class EntryDeleteView(View):
    template_name = "entry_confirm_delete.html"
    success_url = reverse_lazy("entry-list")

    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        return render(request, self.template_name, {'entry': entry})

    def post(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        return redirect(self.success_url)
