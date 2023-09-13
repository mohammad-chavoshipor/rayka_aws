# devices/serializers.py
from rest_framework import serializers

from devices.models import DeviceModel


class DeviceSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    deviceModel = serializers.CharField()
    name = serializers.CharField()
    note = serializers.CharField()
    serial = serializers.CharField()

    def validate_deviceModel(self, value):
        # Check if the DeviceModel with the given ID exists
        try:
            device_model = DeviceModel.get(value)
        except DeviceModel.DoesNotExist:
            raise serializers.ValidationError("DeviceModel does not exist")

        return value


class DeviceModelSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
