from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from channels.models import Category, Channel
from channels.serializers import CategorySerializer, ChannelSerializer


class ChannelListAPIView(ListAPIView):

    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()


class CategoryByChannelListAPIView(ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        name = self.kwargs.get('channel')
        channel = get_object_or_404(Channel, name=name)

        return Category.objects.filter(channel_id=channel.id)
