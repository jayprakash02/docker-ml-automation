from django.shortcuts import render
from django.views.generic import FormView
from .forms import UploadZipFileForm


class UploadView(FormView):
    template_name = 'dashboard/index.html'
    form_class = UploadZipFileForm
    success_url = '/'

    def form_valid(self, form):
        # form.save()
        print("Sucessfully uploaded file")
        return super().form_valid(form)
