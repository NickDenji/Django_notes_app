from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    # Form based on the Note model, so Django can automatically
    # generate form fields from the model fields

    class Meta:
        model = Note  # The model this form is linked to

        # Only include these fields in the form (excludes created_at)
        fields = ['title', 'content']
