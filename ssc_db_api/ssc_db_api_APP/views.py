from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import User as user
from .models import *
from .run import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def load_database(request):
    populate_departments()
    populate_switch01_b01()
    populate_switch02_b01()
    populate_switch01_b02()
    html = "<html><body>DB Loaded.</body></html>"
    return HttpResponse(html)

def clean_database(request):
    Department.objects.all().delete()
    User.objects.all().delete()
    Switch.objects.all().delete()
    Port.objects.all().delete()
    VLAN.objects.all().delete()
    ACL.objects.all().delete()
    Audit_Log.objects.all().delete()
    html = "<html><body>DB Cleaned.</body></html>"
    return HttpResponse(html)

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
    #messages.success(request, f'Account created for {username}, with email {email}!')