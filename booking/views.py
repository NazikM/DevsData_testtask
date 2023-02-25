from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from booking.forms import BookingForm
from booking.models import Booking

TWO_HOURS = timezone.timedelta(hours=2)


class BookingListView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(customer=request.user)
        return render(request, 'booking_list.html', {'bookings': bookings})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(request, "Booking created successfully.")
            return redirect('booking_list')
        else:
            messages.error(request, "Error creating booking.")
        return render(request, 'booking_list.html', {'form': form})


class CancelBookingView(LoginRequiredMixin, View):
    def get(self, request, registration_code):
        booking = get_object_or_404(Booking, registration_code=registration_code)
        return render(request, 'cancel_booking.html', {'booking': booking})

    def post(self, request, registration_code):
        booking = get_object_or_404(Booking, registration_code=registration_code)
        if (booking.event.start_date - timezone.now()) < TWO_HOURS:
            messages.error(request, "The event can only be cancelled up to two hours before the start date.")
        elif (booking.event.end_date - booking.event.start_date) >= TWO_HOURS:
            messages.error(request, "The event must be less than two hours long.")
        else:
            booking.canceled = True
            booking.save()
            messages.success(request, "Booking cancelled successfully.")
        return redirect('booking_list')
