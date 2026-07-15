from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from .models import Note, Like, Comment
from .forms import NoteForm

class DashboardView(ListView):
    model = Note
    template_name = 'notes/dashboard.html'
    context_object_name = 'notes'
    # paginate_by = 10 # Keeps the UI clean and fast

    def get_queryset(self):
        # Only show approved notes to students
        notes = Note.objects.filter(is_approved=True).order_by('-created_at')
        return notes
    
class NoteListView(ListView):
    model = Note
    template_name = 'notes/partials/note_results.html'
    context_object_name = 'notes'

    def get_queryset(self):
        # Only show approved notes to students
        query = self.request.GET.get('q')
        notes = Note.objects.filter(is_approved=True).order_by('-created_at')
        if query:
            notes = notes.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) | 
                Q(subject__name__icontains=query)
            )
        return notes


class MyNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/my_notes.html'
    context_object_name = 'notes'
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
class NoteDetail(DetailView):
    model = Note
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    # fields = ['title', 'description', 'file', 'subject']
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Automatically set the author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'description', 'file']
    success_url = reverse_lazy('dashboard')

    def test_func(self): # Ensure only author can edit
        return self.get_object().author == self.request.user
    
class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.get_object().author == self.request.user


@login_required
def add_comment(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(note=note, author=request.user, content=content)
    return redirect('note-detail', pk=note_id)


def toggle_like(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    # Toggle logic
    like, created = Like.objects.get_or_create(note=note, user=request.user)
    if not created:
        like.delete()
        user_liked = False
    else:
        user_liked = True
    
    # Return ONLY the partial HTML
    return render(request, 'notes/partials/like_button.html', {
        'note': note,
        'user_liked': user_liked
    })