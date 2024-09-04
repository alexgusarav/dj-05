# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorsSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        sensor = request.data
        Sensor(name=sensor['name'], description=sensor['description']).save()
        return Response({'status': 'Датчик добавлен успешно!'})


class SensorView(RetrieveUpdateAPIView):#RetrieveAPIView):#, :
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


@api_view(['POST'])
def add_measurements(request):
    measurement = request.data
    Measurement(sensor=Sensor.objects.get(id = int(measurement['sensor'])), temperature=measurement['temperature']).save()
    return Response({'status': 'Измерение успешно добавлено!'})


