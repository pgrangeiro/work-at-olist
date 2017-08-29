import pytest
from model_mommy import mommy

from channels.serializers import ChannelSerializer


@pytest.mark.django_db
class TestChannelSerializer:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.instance = mommy.make('channels.Channel')

    def test_serializes_instance_correctly(self):
        data = ChannelSerializer(self.instance).data

        assert self.instance.name == data['name']
