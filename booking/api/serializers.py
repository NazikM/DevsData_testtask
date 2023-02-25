import datetime

from django.utils import timezone
from rest_framework import serializers

from booking.models import Booking
TWO_HOURS = datetime.timedelta(hours=2)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['customer']

    def create(self, validated_data):
        booking = Booking(customer=self.context['request'].user, **validated_data)
        booking.save()
        return booking


class BookingCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['registration_code', 'event', 'customer']

    def validate(self, data):
        res = self.instance.event.end_date - self.instance.event.start_date
        print(res, res >= TWO_HOURS)
        if res >= TWO_HOURS:
            raise serializers.ValidationError("The event must be less than two hours long.")
        if (self.instance.event.start_date - timezone.now()).total_seconds() < 7200:
            raise serializers.ValidationError("The event can only be cancelled up to two hours before the start date.")
        return data

    def update(self, instance, validated_data):
        instance.canceled = True
        instance.save()
        return instance
