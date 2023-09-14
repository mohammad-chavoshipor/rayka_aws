from urllib.request import Request
from rest_framework import generics, status

from devices.dynamodb_interface import DynamodbDevices, DynamodbDevicesModel
from .models import Device, DeviceModel
from .serializers import DeviceModelSerializer, DeviceSerializer
from rest_framework.response import Response

# logger
import logging
logger = logging.getLogger(__name__)


class DeviceModelListCreateView(generics.ListCreateAPIView):
    """
        class view create or list data models of devices
    """
    queryset = DeviceModel.scan()
    IDevicesModel = DynamodbDevicesModel()
    serializer_class = DeviceModelSerializer

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            device = self.IDevicesModel.create(serializer.validated_data)
            return Response(self.serializer_class(device).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceListCreateView(generics.ListCreateAPIView):
    """
        class view create or list devicess
    """
    queryset = Device.scan()
    serializer_class = DeviceSerializer
    IDevices = DynamodbDevices()

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            device = self.IDevices.create(data=serializer.validated_data)
            return Response(device, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceRetrieveView(generics.RetrieveAPIView):
    """
        class view retrieve device by id
    """
    queryset = Device
    IDevices = DynamodbDevices()
    serializer_class = DeviceSerializer

    def retrieve(self, request: Request, id: str, *args: tuple, **kwargs: dict) -> Response:
        try:
            # instance = self.queryset.get(id)
            instance = self.IDevices.getById(id)
        except Exception:
            return Response(dict(message="Device Not Found!"), status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
