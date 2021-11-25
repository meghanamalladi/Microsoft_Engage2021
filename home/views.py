from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def upload(request):
    return render(request,'upload.html')

def edit(request):
    return render(request,'edit.html')

def view(request):
    return render(request,'view.html')