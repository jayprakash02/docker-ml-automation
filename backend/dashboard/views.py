from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadZipFileForm
from .models import handle_uploaded_file


class UploadView(FormView):
    template_name = 'dashboard/index.html'
    form_class = UploadZipFileForm
    success_url = '/'

    def upload_file(request):
        if request.method == 'POST':
            form = UploadZipFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadZipFileForm()
        return render(request, 'upload.html', {'form': form})


def gen_zip(pk, name, vars):
    zipObj = ZipFile(os.path.join(
        '/tmp/', str(name) + '_' + str(pk) + '.zip'), 'w')
    zipObj.write(pdf_files[0].path, '/filea.pdf')
    zipObj.write(pdf_files[1].path, '/fileb.pdf')


def aksorder_complete(request, pk):
    ao = get_object_or_404(AksOrder, id=pk)
    zipObj = generate_shop_zip(ao.c.pk, ao.dl, ao.vars)
    ao.zip_file.save('file.zip', zipObj)
