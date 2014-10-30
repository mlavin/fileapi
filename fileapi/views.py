import json

from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseNotFound
from django.views.generic import View


storage = FileSystemStorage()


def file_info(name):
    return {
        'name': name,
        'size': storage.size(name),
        'created': storage.created_time(name),
        'links': {
            'self': reverse('upload-detail', kwargs={'name': name})
        }
    }


class FileListView(View):
    """Get a list of all available files."""

    def get(self, request):
        """List all files."""
        _, files = storage.listdir('')
        info = []
        for name in files:
            info.append(file_info(name))
        result = {
            'files': info,
            'count': len(info),
        }
        return JsonResponse(result)


class FileDetailView(View):
    """Get details for a single file."""

    def get(self, request, name):
        """Get details for a file."""
        if storage.exists(name):
            result = file_info(name)
            return JsonResponse(result)
        else:
            return HttpResponseNotFound()
