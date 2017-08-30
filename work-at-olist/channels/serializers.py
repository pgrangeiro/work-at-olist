from rest_framework import serializers
from channels.models import Category, Channel


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('name', )


class CategoryResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class CategorySerializer(serializers.ModelSerializer):

    parent = CategoryResumeSerializer()
    subcategories = CategoryResumeSerializer(many=True, source='category_set')

    class Meta:
        model = Category
        fields = ('name', 'parent', 'subcategories')
