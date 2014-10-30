from django.conf.urls import url

from .views import FileListView, FileDetailView


urlpatterns = [
    url(r'^uploads/$', FileListView.as_view(), name='upload-list'),
    url(r'^uploads/(?P<name>.*)', FileDetailView.as_view(), name='upload-detail'),
]
