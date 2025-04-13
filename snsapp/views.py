from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import SnsModel

def listfunc(request):
    objects = SnsModel.objects.all()
    for item in objects:
        item.good_minus_one = item.good - 1
        item.read_minus_one = item.read - 1
    return render(request, 'list.html', {'object_list': objects})

def detailfunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def goodfunc(request, pk):
    object = SnsModel.objects.get(pk=pk) 
    object.good += 1
    object.save()
    return redirect('list')

@login_required
def readfunc(request, pk):
    object = SnsModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readers:
        return redirect('list')
    else:
        object.read += 1
        object.readers = object.readers + ' ' + username
        object.save()
        return redirect('list')
    
class SnsCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'text', 'author', 'photo')
    success_url = reverse_lazy('list')

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password =request.POST['password']
        try:
            user = User.objects.create_user(username, "", password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')