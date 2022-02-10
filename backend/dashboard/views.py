from django_zipfile import TemplateZipFile
from django.views.generic import FormView
from .forms import UploadZipFileForm
from .models import Upload


class UploadView(FormView):
    template_name = 'dashboard/index.html'
    form_class = UploadZipFileForm
    success_url = '/'

    def form_valid(self, form):
        new_object = Upload.objects.create(
            file=form.cleaned_data['file']
        )
        return super(UploadView, self).form_valid(form)
