from urllib.request import Request
from rest_framework import generics, status
from .models import Device, DeviceModel
from .serializers import DeviceModelSerializer, DeviceSerializer
from rest_framework.response import Response
import uuid


class DeviceModelListCreateView(generics.ListCreateAPIView):
    """
        class view create or list data models of devices
    """
    queryset = DeviceModel.scan()
    serializer_class = DeviceModelSerializer

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            devices = DeviceModel(id=uuid.uuid4().hex, **
                                  serializer.validated_data)
            devices.save()
            return Response(self.serializer_class(devices).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceListCreateView(generics.ListCreateAPIView):
    """
        class view create or list devicess
    """
    queryset = Device.scan()
    serializer_class = DeviceSerializer

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            devices = Device(id=uuid.uuid4().hex, **
                             serializer.validated_data)
            devices.save()
            return Response(self.serializer_class(devices).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceRetrieveView(generics.RetrieveAPIView):
    """
        class view retrieve device by id
    """
    queryset = Device
    serializer_class = DeviceSerializer

    def retrieve(self, request: Request, id: str, *args: tuple, **kwargs: dict) -> Response:
        try:
            instance = self.queryset.get(id)
        except Exception:
            return Response(dict(message="Device Not Found!"), status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
