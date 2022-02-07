from django.shortcuts import render
from django.views.generic import TemplateView


class UploadView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload'
        return context
