# models.py
from django.db import models
from django.contrib.auth.models import User

class MeetingTranscript(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    therapy_report = models.TextField()
    therapy_session = models.TextField()
    comprehension_report = models.TextField()
    next_session_blueprint = models.CharField(max_length=20)
    goal = models.TextField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
