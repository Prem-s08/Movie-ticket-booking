from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import contacts
from .models import *


def home(request):
    return render(request, 'theater/home.html')

def about(request):
    return render(request, 'theater/about.html', {'title':'About'})

@login_required
def nowshowing(request):
    return render(request, 'theater/nowshowing.html', {'title':'Now Showing'})

def ticketprice(request):
    return render(request, 'theater/ticketprice.html', {'title':'ticket Price'})

def Wonka(request):
    return render(request, 'theater/Wonka.html', {'title':'Wonka'})

def Spiderman(request):
    return render(request, 'theater/Spiderman.html', {'title':'Spider-Man: Across the Spider-Verse'})

def oppenheimer(request):
    return render(request, 'theater/oppenheimer.html', {'title':'Oppenheimer'})

def Trolls(request):
    return render(request, 'theater/Trolls.html', {'title':'Trolls Band Together'})

def contact(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject= request.POST['subject']

        contact=contacts(name=uname, email=email,message=message,subject=subject)
        contact.save()

        return render(request, 'theater/contact.html',{'title':'Contact'})
    else:
        return render(request, 'theater/contact.html',{'title':'Contact'})
    

            
        
        
        
