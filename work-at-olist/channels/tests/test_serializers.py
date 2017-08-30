import pytest
from model_mommy import mommy

from channels.serializers import (
    CategorySerializer, CategoryResumeSerializer, ChannelSerializer
)


@pytest.mark.django_db
class TestChannelSerializer:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.instance = mommy.make('channels.Channel')

    def test_serializes_instance_correctly(self):
        data = ChannelSerializer(self.instance).data

        assert self.instance.name == data['name']


@pytest.mark.django_db
class TestCategoryResumeSerializer:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.instance = mommy.make('channels.Category')

    def test_serializes_instance_correctly(self):
        data = CategoryResumeSerializer(self.instance).data

        assert self.instance.name == data['name']


@pytest.mark.django_db
class TestCategorySerializer:

    @pytest.fixture(autouse=True)
    def set_fixtures(self):
        self.parent = mommy.make('channels.Category')
        self.category = mommy.make('channels.Category')
        self.subcategories = mommy.make('channels.Category', _quantity=2)

    def test_serializes_instance_correctly(self):
        data = CategorySerializer(self.category).data

        assert self.category.name == data['name']
        assert not data['parent']
        assert not data['subcategories']

    def test_serializes_instance_with_parent_correctly(self):
        self.parent.category_set.add(self.category)
        self.parent.save()

        data = CategorySerializer(self.category).data
        expected_parent = CategoryResumeSerializer(self.parent).data

        assert self.category.name == data['name']
        assert expected_parent == data['parent']
        assert not data['subcategories']

    def test_serializes_instance_with_subcategories_correctly(self):
        for c in self.subcategories:
            self.category.category_set.add(c)
            self.category.save()

        data = CategorySerializer(self.category).data
        expected_subcategories = CategoryResumeSerializer(
            self.subcategories, many=True
        ).data

        assert self.category.name == data['name']
        assert not data['parent']
        assert 2 == len(data['subcategories'])
        assert expected_subcategories == data['subcategories']
