from django.conf.urls import url, include
from django.contrib import admin
from appointments import views
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'rest_appointment', views.AppointmentViewSet, "Appointment")

urlpatterns = [
    url(r'^', include('appointments.urls', namespace="appointments")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
