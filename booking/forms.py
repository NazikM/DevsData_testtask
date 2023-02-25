from django import forms

from booking.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].widget.attrs.update({'class': 'form-control'})
