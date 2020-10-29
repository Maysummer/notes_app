from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

class AboutPageView(TemplateView):
    template_name = 'notes/about.html'