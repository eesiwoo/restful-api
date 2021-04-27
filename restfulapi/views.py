from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movies


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer