from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'date','time', 'location', 'image', 'available_seats']

    def get_available_seats(self, obj):
        booked = Booking.objects.filter(event=obj).count()
        total_capacity = 100  # or add a capacity field on Event
        return max(total_capacity - booked, 0)
    

class BookingSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), source='event', write_only=True
    )

    class Meta:
        model = Booking
        fields = ['id', 'event', 'event_id', 'booked_at']