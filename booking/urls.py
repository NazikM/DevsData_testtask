from django.urls import path

from booking.views import BookingListView, CancelBookingView

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),
    path('cancel/<uuid:registration_code>/', CancelBookingView.as_view(), name='cancel_booking'),
]
