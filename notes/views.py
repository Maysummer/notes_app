from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView
from .models import Note

# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

class AboutPageView(TemplateView):
    template_name = 'notes/about.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/post_detail.html'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/note_new.html'
    fields = '__all__'