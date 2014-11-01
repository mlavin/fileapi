import jwt_auth.views

from django.conf.urls import url

from .views import FileListView, FileDetailView, IndexView


urlpatterns = [
    url(r'^uploads/$', FileListView.as_view(), name='upload-list'),
    url(r'^uploads/(?P<name>.*)', FileDetailView.as_view(), name='upload-detail'),
    url(r'^api-token/', jwt_auth.views.obtain_jwt_token, name='api-token'),
    url(r'^$', IndexView.as_view(), name='homepage')
]
