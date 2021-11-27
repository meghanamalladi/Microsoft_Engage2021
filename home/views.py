from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from home.models import Edit,Contact

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

def upload(request):
    return render(request,'upload.html')

def edit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        collegeid = request.POST.get('collegeid')
        email = request.POST.get('email')
        status = request.POST.get('status')
        proof = request.POST.get('proof')
        verificationid = request.POST.get('verificationid')
        edit = Edit(name=name, collegeid = collegeid, email = email, status = status, proof = proof, verificationid = verificationid)
        edit.save()
        #messages.success(request,'Details have been submitted')
        #uploaded_file =  request.FILES['certificate']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        return HttpResponseRedirect("/")
    return render(request,'edit.html')

def view(request):
    vacc_data = Edit.objects.all()
    return render(request,'view.html',{'vacc_data':vacc_data})

#def get_user(request):
    #user_email = request.user.email
    #return user_email
