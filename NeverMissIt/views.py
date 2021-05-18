from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import date

from .models import EventDetails
from .forms import SignUpForm

# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect('NeverMissIt:profilepage')

    else:
        # EventDetails.objects.filter(lastdatetoreg__gt=date.today()).order_by('lastdatetoreg')
        coming_events_in_order = EventDetails.objects.filter(lastdatetoreg__gt=date.today()).order_by('lastdatetoreg')
        context = {'events':coming_events_in_order}
        return render(request, 'NeverMissIt/homepage.html', context)

def signuppage(request):
    if request.user.is_authenticated:
        return redirect('NeverMissIt:profilepage')
    
    else:
        form = SignUpForm()

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created succesfully for ' + form.cleaned_data.get('username'))
                return redirect('NeverMissIt:loginpage')

        context = {'form':form}
        return render(request, 'NeverMissIt/signuppage.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('NeverMissIt:profilepage')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('NeverMissIt:profilepage')
            else :
                messages.info(request, 'username and password does not match')

        context = {}
        return render(request, 'NeverMissIt/loginpage.html', context)

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def logoutpage(request):
    logout(request)
    return redirect('NeverMissIt:loginpage')

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def profilepage(request):
    context = {}
    return render(request, 'NeverMissIt/profilepage.html', context)

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def createeventpage(request):
    context = {}
    return render(request, 'NeverMissIt/createeventpage.html', context)

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def detaileventpage(request):
    context = {}
    return render(request, 'NeverMissIt/detaileventpage.html', context)

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def editeventpage(request):
    context = {}
    return render(request, 'NeverMissIt/editeventpage.html', context)

@login_required(login_url='NeverMissIt:loginpage') # only allowed if " LOGGED IN "
def registereventpage(request):
    context = {}
    return render(request, 'NeverMissIt/registereventpage.html', context)