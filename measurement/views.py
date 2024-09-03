# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, SensorsSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        sensor = request.data
        Sensor(name=sensor['name'], description=sensor['description']).save()
        return Response({'status': 'Датчик добавлен успешно!'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
