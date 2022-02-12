from django.shortcuts import render
from django.views.generic import ListView
from .models import Note

def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/home.html', context)

class NotesListView(ListView):
    model = Note
    template_name = 'notes/home.html'

