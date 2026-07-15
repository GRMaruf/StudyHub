from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/search/', views.NoteListView.as_view(), name='note-list'),
    path('note-detail/<int:pk>', views.NoteDetail.as_view(), name='note-detail'),
    path('my-notes/', views.MyNotesView.as_view(), name='my-notes'),
    path('upload/', views.NoteCreateView.as_view(), name='note-create'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='note-edit'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note-delete'),
    path('toggle_like/<int:note_id>/', views.toggle_like, name='toggle-like'),
    path('add_comment/<int:note_id>/', views.add_comment, name='add-comment'),
]