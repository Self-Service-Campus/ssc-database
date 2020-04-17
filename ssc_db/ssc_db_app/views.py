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


# USER BY DEPARTMENT CODE
class UserByDepartmentCode(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = user.objects.filter(department__code=self.kwargs['post_id'])
        return queryset

# DEPARTMENT
class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# DEPARTMENT BY CODE
class DepartmentByCode(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    def get_queryset(self):
        queryset = Department.objects.filter(code=self.kwargs['post_id'])
        return queryset

# SWITCH
class SwitchView(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

# SWITCH BY CODE
class SwitchByCode(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    def get_queryset(self):
        queryset = Switch.objects.filter(identifier=self.kwargs['post_id'])
        return queryset

# SWITCHES BY MODEL
class SwitchsByModel(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    def get_queryset(self):
        queryset = Switch.objects.filter(model=self.kwargs['post_id'])
        return queryset

# SWITCHES BY DEPARTMENT CODE
class SwitchsByDepartmentCode(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    def get_queryset(self):
        queryset = Switch.objects.filter(department__code=self.kwargs['post_id'])
        return queryset

# PORT
class PortView(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

# PORTS BY SWITCH IDENTIFIER
class PortBySwitchID(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    def get_queryset(self):
        queryset = Port.objects.filter(switch__identifier=self.kwargs['post_id'])
        return queryset

# PORTS BY STATE BY SWITCH ID
class PortBySwtichIDByState(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    def get_queryset(self):
        queryset = Port.objects.filter(switch__identifier=self.kwargs['post_id'], state=self.kwargs['post_id2'])
        return queryset

# PORTS BY IP ADDR
class PortByIPAddr(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    def get_queryset(self):
        queryset = Port.objects.filter(ip_addr=self.kwargs['post_id'])
        return queryset

# VLAN
class VLANView(viewsets.ModelViewSet):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

# VLAN BY ID
class VLANByID(viewsets.ModelViewSet):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer
    def get_queryset(self):
        queryset = VLAN.objects.filter(identifier=self.kwargs['post_id'])
        return queryset

# VLAN BY PORT
class VLANByPort(viewsets.ModelViewSet):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer
    def get_queryset(self):
        queryset = VLAN.objects.filter(port=self.kwargs['post_id'])
        return queryset

# VLAN BY PORT BY SWITCH ID
class VLANByPortBySwitchID(viewsets.ModelViewSet):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer
    def get_queryset(self):
        queryset = VLAN.objects.filter(port=self.kwargs['post_id'], port__switch_id=self.kwargs['post_id2'])
        return queryset

# ACL
class ACLView(viewsets.ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer

# ACL BY ID
class ACLByID(viewsets.ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer
    def get_queryset(self):
        queryset = ACL.objects.filter(id=self.kwargs['post_id'])
        return queryset

# ACL BY EMAIL
class ACLByEmail(viewsets.ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer
    def get_queryset(self):
        queryset = ACL.objects.filter(user__user__email=self.kwargs['post_id'])
        return queryset

# AUDIT
class Audit_LogView(viewsets.ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

# AUDIT BY ID
class Audit_LogByID(viewsets.ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer
    def get_queryset(self):
        queryset = Audit_Log.objects.filter(id=self.kwargs['post_id'])
        return queryset

# AUDIT BY EMAIL
class Audit_LogByEmail(viewsets.ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer
    def get_queryset(self):
        queryset = Audit_Log.objects.filter(user__user__email=self.kwargs['post_id'])
        return queryset
