from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


# Display a list of all notes
def note_list(request):
    # Retrieve all Note objects from the database
    notes = Note.objects.all()

    # Render the list template with the notes data
    return render(request, 'notes/note_list.html', {'notes': notes})


# Display details of a single note
def note_detail(request, pk):
    # Get the note by primary key or return 404 if not found
    note = get_object_or_404(Note, pk=pk)

    # Render the detail template with the note
    return render(request, 'notes/note_detail.html', {'note': note})


# Create a new note
def note_create(request):
    if request.method == 'POST':
        # Bind form with submitted data
        form = NoteForm(request.POST)

        if form.is_valid():
            # Save the new note to the database
            form.save()
            return redirect('note_list')
    else:
        # Create an empty form for GET requests
        form = NoteForm()

    # Render the form template
    return render(request, 'notes/note_form.html', {'form': form})


# Update an existing note
def note_update(request, pk):
    # Retrieve the note to update
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        # Bind form with submitted data and existing instance
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            # Save changes to the note
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        # Pre-fill form with existing note data
        form = NoteForm(instance=note)

    # Render the form template
    return render(request, 'notes/note_form.html', {'form': form})


# Delete a note
def note_delete(request, pk):
    # Retrieve the note to delete
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        # Delete the note from the database
        note.delete()
        return redirect('note_list')

    # Render confirmation page before deletion
    return render(request, 'notes/note_confirm_delete.html', {'note': note})