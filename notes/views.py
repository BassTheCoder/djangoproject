from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="notes/register.html", context={"register_form":form})
