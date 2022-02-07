from django.urls import path
from .views import UploadView

app_name = 'dashboard'

urlpatterns = [
    path('upload', UploadView, name='index'),
]
