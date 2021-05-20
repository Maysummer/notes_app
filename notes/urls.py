from django.urls import path
from .import views
from .views import (AboutPageView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView,)


urlpatterns =[
    path('note/<int:pk>/delete',
        NoteDeleteView.as_view(), name='note_delete'),
    path('note/<int:pk>/edit/',
        NoteUpdateView.as_view(), name='note_edit'),
    path('note/new/', NoteCreateView.as_view(), name='note_new'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', views.index, name='index'),
]
