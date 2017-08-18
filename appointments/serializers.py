from appointments.models import Appointment, Host
from rest_framework import serializers

class HostSerializer(serializers.ModelSerializer):
    # SerializerMethodField automatically uses 'get_' as prefix for field method name.
    #firstname = serializers.SerializerMethodField()
    #lastname  = serializers.SerializerMethodField()
    #middlename  = serializers.SerializerMethodField()

    class Meta:
        model = Host
        fields = ('id','firstname','middlename','lastname')
    
    """
    def get_firstname(self, obj):
        return obj.firstname

    def get_lastname(self, obj):
        return obj.lastname

    def get_middlename(self, obj):
        return obj.middlename
    """

class AppointmentSerializer(serializers.ModelSerializer):
    #host = HostSerializer()
    class Meta:
        model = Appointment
        fields = ('id','host','customer','reason','start_time','end_time')