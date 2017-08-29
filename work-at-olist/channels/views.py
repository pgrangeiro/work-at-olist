from rest_framework.generics import ListAPIView

from channels.models import Channel
from channels.serializers import ChannelSerializer


class ChannelListAPIView(ListAPIView):

    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
