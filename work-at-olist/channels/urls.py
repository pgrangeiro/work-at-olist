from django.conf.urls import url

from channels.views import CategoryByChannelListAPIView, ChannelListAPIView


app_name = 'channels'
urlpatterns = [
    url(r'^$', ChannelListAPIView.as_view(), name='list_channels'),
    url(
        r'^(?P<channel>\w+)/$',
        CategoryByChannelListAPIView.as_view(),
        name='list_categories_by_channel'
    ),
]
