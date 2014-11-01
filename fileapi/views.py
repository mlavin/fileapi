import json

from django import forms
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.generic import View, TemplateView


storage = FileSystemStorage()


class UploadForm(forms.Form):
    name = forms.FileField()


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
    """Get a list of all available files or create a new file."""

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

    def post(self, request):
        """Add a new file."""
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.cleaned_data['name']
            storage.save(upload.name, upload)
            result = file_info(upload.name)
            return JsonResponse(result, status=201)
        else:
            return HttpResponse(form.errors.as_json(), status=400, content_type='application/json')


class FileDetailView(View):
    """Get details for a single file or delete the file."""

    def get(self, request, name):
        """Get details for a file."""
        if storage.exists(name):
            result = file_info(name)
            return JsonResponse(result)
        else:
            return HttpResponseNotFound()

    def delete(self, request, name):
        """Delete a file."""
        if storage.exists(name):
            storage.delete(name)
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=410)


class IndexView(TemplateView):
    template_name = 'index.html'
