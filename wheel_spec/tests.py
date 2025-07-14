from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import WheelSpecification

class WheelSpecAPITestCase(APITestCase):
    def setUp(self):
        self.valid_payload = {
            "formNumber": "FS-101",
            "submittedBy": "Test User",
            "submittedDate": "2025-07-10",
            "fields": {
                "diameter": "40cm",
                "material": "Steel"
            }
        }
        self.invalid_payload = {
            "formNumber": "",
            "submittedBy": "",
            "submittedDate": "2026-01-01",  # future date
            "fields": "not-a-json-object"
        }

    def test_submit_valid_wheel_spec(self):
        url = reverse('submit_wheel_spec')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(WheelSpecification.objects.exists())

    def test_submit_invalid_wheel_spec(self):
        url = reverse('submit_wheel_spec')
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_filtered_specs(self):
        WheelSpecification.objects.create(**self.valid_payload)
        url = reverse('get_filtered_wheel_specs') + "?formNumber=FS-101"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
