from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from home.models import Upload,Contact
from .forms import UploadForm


# Create your views here.
def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        desc = request.POST.get('desc')
        contact=Contact(desc=desc)
        contact.save()
        return HttpResponseRedirect("/")
    return render(request,'contact.html')

def edit(request):
    User = request.user
    user_email = User.email
    Change = Upload.objects.filter(email=user_email)
    Change.delete()
    return HttpResponseRedirect("/upload")

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            print("Error!")
            return HttpResponseRedirect("/")
    else:
        form = UploadForm()
        context = {'form':form}
        return render(request,'upload.html',context)

def view(request):
    User = request.user
    user_email = User.email
    print(User)
    print(user_email)
    vacc_data = Upload.objects.filter(email=user_email)
    print(vacc_data)
    return render(request,'view.html',{'vacc_data':vacc_data})
