from django import forms
from .models import Note
from .validators import validate_file_extension, validate_file_size

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'file', 'subject']
    
    # Apply validators directly to the file field
    file = forms.FileField(validators=[validate_file_extension, validate_file_size])