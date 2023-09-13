from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Device(Model):
    id = UnicodeAttribute(hash_key=True)
    deviceModel = UnicodeAttribute()
    name = UnicodeAttribute()
    note = UnicodeAttribute(null=True)
    serial = UnicodeAttribute()

    class Meta:
        table_name = 'rayka_devices'
        region = 'eu-central-1'


class DeviceModel(Model):
    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()

    class Meta:
        table_name = 'rayka_devices_model'
        region = 'eu-central-1'
