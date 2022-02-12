from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note

def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/home.html', context)

class NotesListView(ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'

class NoteView(DetailView):
    model = Note

