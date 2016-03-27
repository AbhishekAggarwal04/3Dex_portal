from django.shortcuts import render
from content.views import index
from django.template.response import TemplateResponse
from .models import upload
from .forms import UploadForm
from students.models import Student
# Create your views here.
def list(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        instance=''
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            description=request.POST.get('description','')
            newsubmission = upload(file = request.FILES['file'],name=""+request.user.first_name+" "+request.user.last_name,description=description)
            newsubmission.save()
            return index(request)
    else:
        form = UploadForm()
    return TemplateResponse(request,'list.html',{'form': form,'student':instance})


