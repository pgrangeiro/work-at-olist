from django.conf.urls import url

from channels.views import ChannelListAPIView


app_name = 'channels'
urlpatterns = [
    url(r'^$', ChannelListAPIView.as_view(), name='list_channels'),
]
