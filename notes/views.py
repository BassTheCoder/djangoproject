from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Note, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

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

class NoteAddView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)