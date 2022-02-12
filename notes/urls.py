from django.urls import path, include
from .views import NoteAddView, NoteDeleteView, NoteUpdateView, NotesListView, NoteView, NoteAddView, NoteUpdateView, register_request
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', NotesListView.as_view(), name='notes-home'),
    path('register/', register_request, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'notes/logout.html'), name='logout'),
    path('notes/<int:pk>', NoteView.as_view(template_name='notes/note.html'), name='note-view'),
    path('notes/<int:pk>/edit', NoteUpdateView.as_view(), name='note-edit-view'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete-view'),
    path('notes/new', NoteAddView.as_view(), name="note-add")
]