# mcqs/models.py
import uuid
from django.db import models

class MCQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    explanation = models.TextField()
    options = models.JSONField()

