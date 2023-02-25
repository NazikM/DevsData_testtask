from django.urls import path

from booking.api.views import BookingList, CancelBooking

urlpatterns = [
    path('', BookingList.as_view()),
    path('cancel/<uuid:registration_code>', CancelBooking.as_view())
]
