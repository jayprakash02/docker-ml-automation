from django import forms


class UploadZipFileForm(forms.Form):
    file = forms.FileField()
