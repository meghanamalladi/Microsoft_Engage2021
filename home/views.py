from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from home.models import Upload,Contact

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
    upload(request)
    return render(request,'upload.html')

def upload(request):
    if request.method == "POST":
        name = request.POST.get('name')
        collegeid = request.POST.get('collegeid')
        email = request.POST.get('email')
        status = request.POST.get('status')
        proof = request.POST.get('proof')
        verificationid = request.POST.get('verificationid')
        edit = Upload(name=name, collegeid = collegeid, email = email, status = status, proof = proof, verificationid = verificationid)
        edit.save()
        #messages.success(request,'Details have been submitted')
        #uploaded_file =  request.FILES['certificate']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        return HttpResponseRedirect("/services")
    return render(request,'upload.html')

def view(request):
    User = request.user
    user_email = User.email
    print(User)
    print(user_email)
    vacc_data = Upload.objects.filter(email=user_email)
    print(vacc_data)
    return render(request,'view.html',{'vacc_data':vacc_data})
