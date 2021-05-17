from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    return render(request, 'NeverMissIt/homepage.html', context)

def signuppage(request):
    context = {}
    return render(request, 'NeverMissIt/signuppage.html', context)

def loginpage(request):
    context = {}
    return render(request, 'NeverMissIt/loginpage.html', context)

def profilepage(request):
    context = {}
    return render(request, 'NeverMissIt/profilepage.html', context)

def createeventpage(request):
    context = {}
    return render(request, 'NeverMissIt/createeventpage.html', context)

def detaileventpage(request):
    context = {}
    return render(request, 'NeverMissIt/detaileventpage.html', context)

def editeventpage(request):
    context = {}
    return render(request, 'NeverMissIt/editeventpage.html', context)

def registereventpage(request):
    context = {}
    return render(request, 'NeverMissIt/registereventpage.html', context)