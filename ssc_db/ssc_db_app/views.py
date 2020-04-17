from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import User as user

# Create your views here.
def index(request):
    return render(request, 'index.html')

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



# ----- REST FRAMEWORK -----
# USER
class UserView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

# DEPARTMENT
class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# SWITCH
class SwitchView(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

# PORT
class PortView(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

# VLAN
class VLANView(viewsets.ModelViewSet):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

# ACL
class ACLView(viewsets.ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer

# AUDIT
class Audit_LogView(viewsets.ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer