from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Edit

# Create your views here.
def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
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
    return render(request,'edit.html')

def view(request):
    return render(request,'view.html')