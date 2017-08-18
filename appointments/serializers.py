from appointments.models import Appointment, Host
from rest_framework import serializers

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('id','firstname','middlename','lastname')

class AppointmentSerializer(serializers.ModelSerializer):
    host = HostSerializer()
    class Meta:
        model = Appointment
        fields = ('id','host','customer','reason','start_time','end_time')