from ..serializers import *
from rest_framework import generics
from ..models import User as user
from ..models import *
from ..run import *


# ----- REST FRAMEWORK -----
# --- USER ---
class UserView(generics.ListCreateAPIView):
	queryset = user.objects.all()
	serializer_class = UserSerializer

# USER BY DEPARTMENT ACRON
class UserByDepartmentAcron(generics.ListCreateAPIView):
	queryset = user.objects.all()
	serializer_class = UserSerializer

	def get_queryset(self):
		acron = self.request.query_params.get('post_id')

		queryset = user.objects.filter(department__acron_dep=acron)
		return queryset


# --- DEPARTMENT ---
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


# --- SWITCH ---
class SwitchView(generics.ListCreateAPIView):
	queryset = Switch.objects.all()
	serializer_class = SwitchSerializer

# SWITCH BY ID_SWITCH
class SwitchById(generics.ListCreateAPIView):
	queryset = Switch.objects.all()
	serializer_class = SwitchSerializer

	def get_queryset(self):
		queryset = Switch.objects.filter(id_switch=self.kwargs['post_id'])
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


# --- PORT ---
class PortView(generics.ListCreateAPIView):
	queryset = Port.objects.all()
	serializer_class = PortSerializer

# PORT BY ID
class PortById(generics.ListCreateAPIView):
	queryset = Port.objects.all()
	serializer_class = PortSerializer

	def get_queryset(self):
		queryset = Port.objects.filter(id_port=self.kwargs['post_id'])
		return queryset

# PORTS BY SWITCH ID
class PortBySwitchID(generics.ListCreateAPIView):
	queryset = Port.objects.all()
	serializer_class = PortSerializer

	def get_queryset(self):
		queryset = Port.objects.filter(switch__id_switch=self.kwargs['post_id'])
		return queryset

# PORTS BY STATE BY SWITCH ID
class PortBySwtichIDByState(generics.ListCreateAPIView):
	queryset = Port.objects.all()
	serializer_class = PortSerializer

	def get_queryset(self):
		queryset = Port.objects.filter(switch__id_switch=self.kwargs['post_id'], state_port=self.kwargs['post_id2'])
		return queryset


# --- VLAN ---
class VLANView(generics.ListCreateAPIView):
	queryset = VLAN.objects.all()
	serializer_class = VLANSerializer

# VLAN BY ID
class VLANByID(generics.ListCreateAPIView):
	queryset = VLAN.objects.all()
	serializer_class = VLANSerializer

	def get_queryset(self):
		queryset = VLAN.objects.filter(id_vlan=self.kwargs['post_id'])
		return queryset

# VLAN BY PORT ID
class VLANByPortID(generics.ListCreateAPIView):
	queryset = VLAN.objects.all()
	serializer_class = VLANSerializer

	def get_queryset(self):
		queryset = VLAN.objects.filter(port__id_port=self.kwargs['post_id'])
		return queryset

# VLAN BY PORT NUMBER BY SWITCH ID
class VLANByPortNumberBySwitchID(generics.ListCreateAPIView):
	queryset = VLAN.objects.all()
	serializer_class = VLANSerializer

	def get_queryset(self):
		queryset = VLAN.objects.filter(port__number_port=self.kwargs['post_id'], port__switch__id_switch=self.kwargs['post_id2'])
		return queryset


# --- ACL ---
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


# --- AUDIT ---
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
