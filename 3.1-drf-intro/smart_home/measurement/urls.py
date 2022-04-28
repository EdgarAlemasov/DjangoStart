from django.urls import path

from measurement.views import SensorCreateAPIView, SensorUpdateAPIView, MeasurementCreateAPIView

urlpatterns = [
    path('sensor/', SensorCreateAPIView.as_view(), name='create_sensor'),
    path('sensor/<pk>/', SensorUpdateAPIView.as_view(), name='update_sensor'),
    path('measurement/', MeasurementCreateAPIView.as_view(), name='add_measurement'),
]
