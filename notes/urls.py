from django.urls import path, include
from .views import NotesListView, NoteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', NotesListView.as_view(), name='notes-home'),
    path('', include('django_registration.backends.one_step.urls')),
    path('login', auth_views.LoginView.as_view(template_name = 'notes/login.html'), name='login'),
    path('notes/<int:pk>', NoteView.as_view(template_name='notes/note.html'), name='note-view'),
]