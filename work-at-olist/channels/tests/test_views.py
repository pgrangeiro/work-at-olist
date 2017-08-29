import pytest

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APIClient

from channels.serializers import ChannelSerializer


@pytest.mark.django_db
class TestChannelListAPIView:

    def setup_method(self, test_method):
        self.url = reverse('channels:list_channels')
        self.client = APIClient()

    def test_view_get_returns_response_successfully(self):
        response = self.client.get(self.url)

        assert status.is_success(response.status_code)
        assert [] == response.data

    def test_view_get_list_channels_correctly(self):
        instances = mommy.make('channels.Channel', _quantity=2)
        expected = ChannelSerializer(instances, many=True).data

        response = self.client.get(self.url)

        assert 2 == len(response.data)
        assert expected == response.data
