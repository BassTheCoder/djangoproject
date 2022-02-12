from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse

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

class RegisterView(RegistrationView):
    success_url = '/'

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('note-view', args=[str(self.id)])

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = "/"

    def get_absolute_url():
        return reverse('notes-home')
