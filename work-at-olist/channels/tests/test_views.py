import pytest

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APIClient

from channels.serializers import CategorySerializer, ChannelSerializer


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


@pytest.mark.django_db
class TestCategoryByChannelListAPIView:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.channel = mommy.make('channels.Channel', name='xpto')

    def setup_method(self, test_method):
        self.url = reverse(
            'channels:list_categories_by_channel',
            kwargs={'channel': 'xpto'},
        )
        self.client = APIClient()

    def test_view_get_returns_response_successfully(self):
        response = self.client.get(self.url)

        assert status.is_success(response.status_code)
        assert [] == response.data

    def test_view_get_returns_404_when_channel_does_not_exist(self):
        url = reverse(
            'channels:list_categories_by_channel',
            kwargs={'channel': 'test'},
        )

        response = self.client.get(url)
        assert status.is_client_error(response.status_code)

    def test_view_get_list_channels_correctly(self):
        instances = mommy.make('channels.Category', _quantity=2)
        for c in instances:
            self.channel.category_set.add(c)
        self.channel.save()

        expected = CategorySerializer(instances, many=True).data

        response = self.client.get(self.url)

        assert 2 == len(response.data)
        assert expected == response.data


@pytest.mark.django_db
class TestCategoryAPIView:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.category = mommy.make('channels.Category', name='xpto')

    def setup_method(self, test_method):
        self.url = reverse(
            'channels:category_detail',
            kwargs={'category': 'xpto'},
        )
        self.client = APIClient()

    def test_view_get_returns_response_successfully(self):
        response = self.client.get(self.url)

        assert status.is_success(response.status_code)
        assert response.data

    def test_view_get_returns_404_when_channel_does_not_exist(self):
        url = reverse(
            'channels:category_detail',
            kwargs={'category': 'test'},
        )

        response = self.client.get(url)
        assert status.is_client_error(response.status_code)

    def test_view_get_list_channels_correctly(self):
        expected = CategorySerializer(self.category).data

        response = self.client.get(self.url)

        assert expected == response.data
