from django.urls import path
from .views import *

urlpatterns = [
    path('create_notes/', NoteCreateAPIView.as_view(), name='note-create'),
    path('get_notes/', NoteListAPIView.as_view(), name='note-list'),
    path('get_notes/<int:pk>/', NoteRetrieveAPIView.as_view(), name='note-retrieve'),
    path('edit_notes/<int:pk>/', NoteUpdateAPIView.as_view(), name='note-update'),
    path('del_notes/<int:pk>/', NoteDestroyAPIView.as_view(), name='note-destroy'),
    path('share_notes/', NoteShareAPIView.as_view(), name='note-share'),
    path('get_shared_notes/', SharedNoteListAPIView.as_view(), name='shared-note-list'),
    path('get_received_notes/', ReceivedNoteListAPIView.as_view(), name='received-note-list'),

]

