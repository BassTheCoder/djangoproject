from django.urls import path, include
from .views import NoteAddView, NotesListView, NoteView, NoteAddView
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView 


urlpatterns = [
    path('', NotesListView.as_view(), name='notes-home'),
    path('register', RegistrationView.as_view(template_name = 'notes/register.html'), name='register'),
    path('login', auth_views.LoginView.as_view(template_name = 'notes/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'notes/logout.html'), {'next_page': ''}, name='logout'),
    path('notes/<int:pk>', NoteView.as_view(template_name='notes/note.html'), name='note-view'),
    path('notes/new', NoteAddView.as_view(), name="note-add")
]