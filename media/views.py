from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import QcowForm
from .models import Qcow
#from django.views.decorators.csrf import csrf_exempt


class Home(TemplateView):
    template_name = 'home.html'

# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)


def qcow_list(request):
    qcows = Qcow.objects.all()
    return render(request, 'qcow_list.html', {
        'qcows': qcows
    })

def upload_qcow(request):
    if request.method == 'POST':
      form = QcowForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('qcow_list')
    else:
          form = QcowForm()    
    return render(request, 'upload_qcow.html', {
        'form': form
    })

def delete_qcow(request, pk):
    if request.method == 'POST':
        qcow = Qcow.objects.get(pk=pk)
        qcow.delete()
    return redirect('qcow_list')
