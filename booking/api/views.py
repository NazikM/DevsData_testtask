from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from booking.api.serializers import BookingSerializer, BookingCancelSerializer
from booking.models import Booking


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class CancelBooking(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCancelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'registration_code'
