from django.urls import path

from measurement.views import SensorsView, SensorView, add_measurements#, change_sensor

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', add_measurements),
]
