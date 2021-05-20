from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Note

# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

class AboutPageView(TemplateView):
    template_name = 'notes/about.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/note_new.html'
    fields = '__all__'

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note_edit.html'
    fields = ['title', 'text']

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'
    success_url = reverse_lazy(index)