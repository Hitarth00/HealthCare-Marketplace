from django.contrib import messages
from django.shortcuts import render
from .models import contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def indextwo(request):
    return render(request,'index-2.html')

def contactus(request):
    return render(request,'contact.html')

def insertdata(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        query= contact(name=name, email=email,subject=subject,phone=phone,message=message)
        query.save()
        messages.success(request,"DATA INSERTED SUCCESSFULLY")
    else:
        messages.error(request,"ERROR OCCURED!!")
    return render(request,'contact.html')



