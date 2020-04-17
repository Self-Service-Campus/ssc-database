from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from .serializers import *
from rest_framework import viewsets, generics
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
class UserView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


# USER BY DEPARTMENT ACRON
class UserByDepartmentAcron(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        print(self.kwargs['post_id'])
        queryset = user.objects.filter(department__acron_dep=self.kwargs['post_id'])
        return queryset

# DEPARTMENT
class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# DEPARTMENT BY ACRON
class DepartmentByAcron(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.filter(acron_dep=self.kwargs['post_id'])
        return queryset

# SWITCH
class SwitchView(generics.ListCreateAPIView):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

# SWITCH BY CODE
class SwitchByIdentifier(generics.ListCreateAPIView):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

    def get_queryset(self):
        queryset = Switch.objects.filter(identifier_switch=self.kwargs['post_id'])
        return queryset

# SWITCHES BY MODEL
class SwitchsByModel(generics.ListCreateAPIView):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

    def get_queryset(self):
        queryset = Switch.objects.filter(model_switch=self.kwargs['post_id'])
        return queryset

# SWITCHES BY DEPARTMENT ACRON
class SwitchsByDepartmentAcron(generics.ListCreateAPIView):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

    def get_queryset(self):
        queryset = Switch.objects.filter(department__acron_dep=self.kwargs['post_id'])
        return queryset

# PORT
class PortView(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

# PORTS BY SWITCH IDENTIFIER
class PortBySwitchID(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

    def get_queryset(self):
        queryset = Port.objects.filter(switch__identifier=self.kwargs['post_id'])
        return queryset

# PORTS BY STATE BY SWITCH ID
class PortBySwtichIDByState(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

    def get_queryset(self):
        queryset = Port.objects.filter(switch__identifier=self.kwargs['post_id'], state=self.kwargs['post_id2'])
        return queryset

# PORTS BY IP ADDR
class PortByIPAddr(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

    def get_queryset(self):
        queryset = Port.objects.filter(ip_addr_port=self.kwargs['post_id'])
        return queryset

# VLAN
class VLANView(generics.ListCreateAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

# VLAN BY ID
class VLANByID(generics.ListCreateAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

    def get_queryset(self):
        queryset = VLAN.objects.filter(identifier_vlan=self.kwargs['post_id'])
        return queryset

# VLAN BY PORT
class VLANByPort(generics.ListCreateAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

    def get_queryset(self):
        # tenho umas duvidas aqui, by port ip address talvez pq by port tem de ir buscar
        # o object inteiro
        # TODO: Ignorar por enquanto
        queryset = VLAN.objects.filter(port=self.kwargs['post_id'])
        return queryset

# VLAN BY PORT BY SWITCH ID
class VLANByPortBySwitchID(generics.ListCreateAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

    def get_queryset(self):
        queryset = VLAN.objects.filter(port__number_port=self.kwargs['post_id'], port__identifier_switch=self.kwargs['post_id2'])
        return queryset

# ACL
class ACLView(generics.ListCreateAPIView):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer

# ACL BY ID
class ACLByID(generics.ListCreateAPIView):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer

    def get_queryset(self):
        queryset = ACL.objects.filter(id_acl=self.kwargs['post_id'])
        return queryset

# ACL BY EMAIL
class ACLByEmail(generics.ListCreateAPIView):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer

    def get_queryset(self):
        queryset = ACL.objects.filter(user__user__email=self.kwargs['post_id'])
        return queryset

# AUDIT
class Audit_LogView(generics.ListCreateAPIView):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

# AUDIT BY ID
class Audit_LogByID(generics.ListCreateAPIView):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

    def get_queryset(self):
        queryset = Audit_Log.objects.filter(id_audit=self.kwargs['post_id'])
        return queryset

# AUDIT BY EMAIL
class Audit_LogByEmail(generics.ListCreateAPIView):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

    def get_queryset(self):
        queryset = Audit_Log.objects.filter(user__user__email=self.kwargs['post_id'])
        return queryset
