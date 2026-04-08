from django.db import models


class Note(models.Model):
    # The title of the note (short text, max 200 characters)
    title = models.CharField(max_length=200)

    # The main body/content of the note (no length limit)
    content = models.TextField()

    # Automatically stores the date and time when the note is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns the title when the object is displayed (e.g., in Django admin)
        return self.title

