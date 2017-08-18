from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import json
import datetime
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

class AppointmentView(generic.ListView):
    template_name = 'appointments/index.html'
    context_object_name = 'display_the_calendar'

    def get_queryset(self):
        return Appointment.objects.all();

class AppointmentViewSet(viewsets.ModelViewSet):

    """

    API endpoint that adds, modifies, and deletes appointments.

    """
    queryset = Appointment.objects.all()
    model = Appointment
    serializer_class = AppointmentSerializer

    def retrieve(self, request, pk=None):
        queryset = Appointment.objects.all()
        apt = get_object_or_404(queryset, pk=pk)
        serializer = AppointmentSerializer(apt)

        return Response(serializer.data)

    def list(self, request):
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request):
        serializer = AppointmentSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        snip = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(snip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        temp = self.get_object(pk)
        serializer = AppointmentSerializer(temp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request, pk):
        destr = Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(destr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            destr.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
