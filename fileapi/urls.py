from django.conf.urls import url

from .views import FileListView, FileDetailView, IndexView


urlpatterns = [
    url(r'^uploads/$', FileListView.as_view(), name='upload-list'),
    url(r'^uploads/(?P<name>.*)', FileDetailView.as_view(), name='upload-detail'),
    url(r'^$', IndexView.as_view(), name='homepage')
]
