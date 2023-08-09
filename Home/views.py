from django.shortcuts import render
from django.http import HttpResponse
from Home.models  import contact

# Create your views here.
def Home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get()
    return render(request,'index.html')

def About(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio.html') 