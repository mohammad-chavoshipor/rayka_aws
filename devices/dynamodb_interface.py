import json
import logging

from nanoid import generate
from rayka.settings import NANO_ID as _A
from .models import Device, DeviceModel
from pynamodb.expressions.operand import Path

logger = logging.getLogger(__name__)


class DynamodbDevicesModel:
    def __init__(self) -> None:
        if not DeviceModel.exists():
            DeviceModel.create_table(wait=True)
            logger.info("created the Device-Model-table")

    def create(self, data: dict, keepID: bool = False):
        device_model = DeviceModel()
        if 'id' in data.keys() and keepID:
            id = data['id']
        else:
            id = generate(_A, 13)
        while self.checkPkExists(id=id):
            id = generate(_A, 13)

        device_model.from_json(json.dumps(data))
        device_model.id = id
        device_model.save()
        keys = {"id": id, **data}
        return keys

    def getById(self, id: str):
        entity = DeviceModel.get(hash_key=id)
        return entity

    def checkPkExists(self, id: str):
        try:
            return DeviceModel.get(hash_key=id).exists()
        except Exception as e:
            logger.exception(e)
            return False


class DynamodbDevices:
    def __init__(self) -> None:
        if not Device.exists():
            Device.create_table(wait=True)
            logger.info("created the Device-table")

    def create(self, data: dict, keepID: bool = False):
        device = Device()
        if 'id' in data.keys() and keepID:
            id = data['id']
        else:
            id = generate(_A, 13)
        while self.checkPkExists(id=id):
            id = generate(_A, 13)

        device.from_json(json.dumps(data))
        device.id = id
        device.save()
        keys = {"id": id, **data}
        return keys

    def getById(self, id: str):
        entity = Device.get(hash_key=id)
        return entity

    def checkPkExists(self, id: str):
        try:
            return Device.get(hash_key=id).exists()
        except Exception as e:
            logger.exception(e)
            return False
