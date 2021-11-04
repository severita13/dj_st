from django.db.models.query import QuerySet
from rest_framework import generics, serializers

from applications.music.models import Music
from applications.music.serializers import MusicSerializer

class SongsListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
