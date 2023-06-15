from rest_framework import serializers
from .models import Note, SharedNote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class SharedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNote
        fields = '__all__'

class SharedNoteListSerializer(serializers.ModelSerializer):
    note = NoteSerializer()
    class Meta:
        model = SharedNote
        fields = '__all__'