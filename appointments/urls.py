from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from appointments import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from django.contrib.auth.models import User
from rest_framework import viewsets, routers
from appointments.serializers import AppointmentSerializer
from django.dispatch import receiver

router = routers.DefaultRouter()
router.register(r'rest_appointment', views.AppointmentViewSet, "Appointment")

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

urlpatterns = patterns('',
    url(r'^$', views.AppointmentView.as_view(), name='calendar_home'),
    url(r'^', include(router.urls)),
)

urlpatterns += staticfiles_urlpatterns()