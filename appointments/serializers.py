from appointments.models import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id','host','customer','reason','start_time','end_time')