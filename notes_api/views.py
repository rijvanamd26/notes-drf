from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Note, SharedNote
from .serializers import NoteSerializer, SharedNoteSerializer, SharedNoteListSerializer

class NoteCreateAPIView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteListAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteDestroyAPIView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteShareAPIView(generics.CreateAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    

class SharedNoteListAPIView(generics.ListAPIView):
    serializer_class = SharedNoteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SharedNote.objects.filter(sender=user)

class ReceivedNoteListAPIView(generics.ListAPIView):
    serializer_class = SharedNoteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SharedNote.objects.filter(receiver=user)
    
# class NoteListAPIView(generics.ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteUpdateAPIView(generics.UpdateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteDestroyAPIView(generics.DestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteShareAPIView(generics.CreateAPIView):
#     queryset = SharedNote.objects.all()
#     serializer_class = SharedNoteSerializer
