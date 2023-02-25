from rest_framework import generics

from events.api.serializers import EventSerializer
from events.models import Event
from events.permissions import IsAdminOrReadOnly


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]


