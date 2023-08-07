from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def About(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio.html')