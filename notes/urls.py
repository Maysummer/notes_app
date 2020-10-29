from django.urls import path

from .import views
from .views import AboutPageView


urlpatterns =[
    path('about/', AboutPageView.as_view(), name='about'),
    path('', views.index, name='index'),
]