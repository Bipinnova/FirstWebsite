from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1" : "Durgesh Sir is Great-----",
        "variable2" : "Ajay bro also is Great-----"
    }

    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def agreement(request):
    return render(request, 'agreement.html')

def support(request):
    return render(request, 'support.html')

def career(request):
    return render(request, 'career.html')

def performance(request):
    return render(request, 'performance.html')

def incident(request):
    return render(request, 'incident.html')

def microlearning(request):
    return render(request, 'microlearning.html')

def ergonomic(request):
    return render(request, 'ergonomic.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")


    return render(request, 'contact.html')
    #return HttpResponse("this is contact page") 