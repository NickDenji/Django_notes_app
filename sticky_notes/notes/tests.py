from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):

    def test_note_creation(self):
        """
        Test that a Note object can be created successfully
        and that its title is stored correctly.
        """
        note = Note.objects.create(title="Test", content="Hello")
        self.assertEqual(note.title, "Test")

    
    def test_str_method(self):
        """
        Test that the string representation of the Note
        returns the title (as defined in __str__).
        """
        note = Note(title="My Note")
        self.assertEqual(str(note), "My Note")


class NoteViewsTest(TestCase):

    def setUp(self):
        """
        This method runs before each test.
        It creates a sample note that can be used in tests.
        """
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )

    
    def test_note_list_view(self):
        """
        Test the 'View Notes' use case.
        Ensures the note list page loads correctly
        and displays existing notes.
        """
        response = self.client.get(reverse("note_list"))

        # Check page loads successfully
        self.assertEqual(response.status_code, 200)

        # Check the note appears on the page
        self.assertContains(response, "Test Note")

    
    def test_note_detail_view(self):
        """
        Test the 'View Note Detail' use case.
        Ensures a specific note can be viewed.
        """
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )

        # Check page loads successfully
        self.assertEqual(response.status_code, 200)

        # Check correct note content is displayed
        self.assertContains(response, "Test Note")

    
    def test_note_create_view(self):
        """
        Test the 'Create Note' use case.
        Ensures a new note can be created successfully.
        """
        response = self.client.post(
            reverse("note_create"),
            {
                'title': 'New Note',
                'content': 'New Content'
            }
        )

        # After successful creation, should redirect
        self.assertEqual(response.status_code, 302)

        # Check that a new note was added to the database
        self.assertEqual(Note.objects.count(), 2)

    
    def test_note_update_view(self):
        """
        Test the 'Edit Note' use case.
        Ensures an existing note can be updated.
        """
        response = self.client.post(
            reverse("note_update", args=[self.note.id]),
            {
                'title': 'Updated Note',
                'content': 'Updated Content'
            }
        )

        # After update, should redirect
        self.assertEqual(response.status_code, 302)

        # Refresh object from database and check update
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")

    
    def test_note_delete_view(self):
        """
        Test the 'Delete Note' use case.
        Ensures a note can be deleted successfully.
        """
        response = self.client.post(
            reverse("note_delete", args=[self.note.id])
        )

        # After deletion, should redirect
        self.assertEqual(response.status_code, 302)

        # Check that the note was removed from the database
        self.assertEqual(Note.objects.count(), 0)
