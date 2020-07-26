from django.shortcuts import render, HttpResponse
from  datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

# only render the block not httpResponse


def index(request):
    value={
        "variable":"chanchal"
    }
    # messages.success(request,"this is a text message")
    # return HttpResponse("this is home page")
    return render(request, 'index.html',value)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

# def services(requestc):
#     return render(request, 'index.html')
#     # return HttpResponse("this is services page")

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        messages.success(request, 'Your message is sent!')

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")




