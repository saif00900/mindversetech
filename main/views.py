from django.shortcuts import render
from django.http import HttpResponse
from main.models import ServiceIcon
from main.models import Portfolio
from main.models import AboutUs
from main.models import Enquiry

# Create your views here.
def home(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        info = Enquiry(name=name,number=number,email=email,msg=msg)
        info.save()
        services = ServiceIcon.objects.all()
        portfolio = Portfolio.objects.all()
        about = AboutUs.objects.all()
        target = "Query Submitted :) , We'll Contact You Soon At Whatsapp Or Email"
        data = {
            'services' : services ,
            'portfolio' : portfolio ,
            'about' : about ,
            'target' : target
                }
        return render(request, 'index.html', data)
    # getting data from db :
    services = ServiceIcon.objects.all()
    portfolio = Portfolio.objects.all()
    about = AboutUs.objects.all()
    data = {
        'services' : services ,
        'portfolio' : portfolio ,
        'about' : about ,
    }
    return render(request, 'index.html', data)
