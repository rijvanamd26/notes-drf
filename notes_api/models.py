from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

def validate_audio(value):
    file_extension = value.name.split('.')[-1]
    if file_extension.lower() not in ['mp3', 'wav']:
        raise ValidationError('Invalid audio file. Only MP3 and WAV files are allowed.')

def validate_video(value):
    file_extension = value.name.split('.')[-1]
    if file_extension.lower() not in ['mp4', 'avi', 'mov']:
        raise ValidationError('Invalid video file. Only MP4, AVI, and MOV files are allowed.')

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    audio = models.FileField(blank=True, null=True, upload_to='uploads/', validators=[validate_audio])
    video = models.FileField(blank=True, null=True, upload_to='uploads/', validators=[validate_video])

    def __str__(self):
        return self.title


class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.sender.username + ' sent to ' + self.receiver.username
    