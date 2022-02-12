from django.urls import path
from . import views
from .views import NotesListView

urlpatterns = [
    path('', NotesListView.as_view(), name='notes-home'),
]