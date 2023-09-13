from django.test import TestCase

from devices.views import DeviceListCreateView, DeviceModelListCreateView, DeviceRetrieveView
from .models import DeviceModel
import uuid
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory


class DeviceModelTestCase(TestCase):
    def setUp(self):
        self.device_model_data = {
            "name": "Model 1",
        }
        self.factory = APIRequestFactory()
        self.model_view = DeviceModelListCreateView.as_view()

    def create_device_model(self):
        # Helper method to create a device model and set device_model_id.
        request = self.factory.post(
            "/api/models/", data=self.device_model_data, format="json")
        response = self.model_view(request)
        return response, response.data

    def test_create_device_model_success(self):
        # Send a POST request to create a device model.
        response, response_data = self.create_device_model()

        # Check if the response status code is 201 (Created).
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the created object's name matches the expected value.
        self.assertEqual(response_data['name'], "Model 1")

        device_model = DeviceModel.get(response_data['id'])
        device_model.delete()


class DeviceTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "deviceModel": "",
            "name": "Test Name",
            "note": "Note 1",
            "serial": "Serial 2"
        }
        self.view_device = DeviceListCreateView.as_view()
        self.model_view = DeviceModelListCreateView.as_view()
        self.device_retrieve = DeviceRetrieveView.as_view()
        self.factory = APIRequestFactory()

    def test_bad_request_create_divce(self):
        request = self.factory.post("/api/devices/", self.data, format="json")
        response = self.view_device(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("deviceModel", response.data)

    def test_bad_request_retrieve_divce(self):
        request = self.factory.get(
            "/api/devices/{}/".format(0), self.data, format="json")
        response = self.device_retrieve(request, 0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertDictEqual(response.data, {'message': 'Device Not Found!'})

    def test_success_request_retrieve_divce(self):
        # first create model
        request_model = self.factory.post(
            "/api/models/", {"name": "Test Model"}, format="json")
        response_model = self.model_view(request_model)
        self.data['deviceModel'] = response_model.data['id']
        request = self.factory.post("/api/devices/", self.data, format="json")
        response_create = self.view_device(request)

        request = self.factory.get(
            "/api/devices/{}/".format(response_create.data['id']), self.data, format="json")
        response = self.device_retrieve(request, response_create.data['id'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)

    def test_success_request_create_divce(self):
        # first create model
        request_model = self.factory.post(
            "/api/models/", {"name": "Test Model"}, format="json")
        response_model = self.model_view(request_model)
        self.data['deviceModel'] = response_model.data['id']
        request = self.factory.post("/api/devices/", self.data, format="json")
        view = DeviceListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
