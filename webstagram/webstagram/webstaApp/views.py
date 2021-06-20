from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.http import HttpResponse
from django.utils import timezone
from .models import Feed
# Create your views here.

def home(request):
    return render(request,'feed.html')
    
def feed(request):
    return render(request,'feed.html')
    
def login(request):
    if request.method=="POST" :
        username= request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(request, username=username, password=password)

        if username is not None:
            auth.login(request, user)
            return redirect('feed')
        else:
            return render(request, 'login.html',{'error' : 'username or password is incorrect. '})
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')


def create(request):
    new_Feed=Feed()
    new_Feed.pub_date=timezone.datetime.now()
    new_Feed.text=request.POST['text']
    new_Feed.image= request.FILES['image']
    new_Feed.author=request.user
    new_Feed.save()
    return redirect('home')

def update(request, feed_id):
    return redirect('home')