from django.conf.urls import url

from channels.views import (
    CategoryAPIView, CategoryByChannelListAPIView, ChannelListAPIView,
)


app_name = 'channels'
urlpatterns = [
    url(r'^$', ChannelListAPIView.as_view(), name='list_channels'),
    url(
        r'^(?P<channel>\w+)/categories/$',
        CategoryByChannelListAPIView.as_view(),
        name='list_categories_by_channel'
    ),
    url(
        r'^categories/(?P<category>\w+)/$',
        CategoryAPIView.as_view(),
        name='category_detail'
    ),
]
