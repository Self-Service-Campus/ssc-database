from django.conf.urls import url
from django.urls import path, include
from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="SSC API DOCUMENTATION")

urlpatterns = [

	# SWAGGER
	path('api_doc/', schema_view),

	# --- API ENDPOINTS ---
	# USER
	url('user', views.UserView.as_view()),
	# USER BY DEPARTMENT CODE
	url(r'^user/dep/(?P<post_id>\w+)$', views.UserByDepartmentAcron.as_view()),
	# DEPARTMENT
	url('department', views.DepartmentView.as_view()),
	# DEPARTMENT BY CODE
	url(r'^department/(?P<post_id>\w+)$', views.DepartmentByAcron.as_view()),
	# SWITCH
	url('switch', views.SwitchView.as_view()),
	# SWITCH BY CODE
	url(r'^switch/code/(?P<post_id>\w+)$', views.SwitchByIdentifier.as_view()),
	# SWITCHES BY MODEL
	url(r'^switch/model/(?P<post_id>\w+)$', views.SwitchsByModel.as_view()),
	# SWITCHES BY DEPARTMENT CODE
	url(r'^switch/dep/(?P<post_id>\w+)$', views.SwitchsByDepartmentAcron.as_view()),
	# PORTS
	url('port', views.PortView.as_view()),
	# PORTS BY SWITCH IDENTIFIER
	url(r'^port/switch/(?P<post_id>\w+)$', views.PortBySwitchID.as_view()),
	# PORTS BY STATE BY SWITCH ID
	url(r'^port/switch/(?P<post_id>\w+)/state/(?P<post_id2>\w+)$', views.PortBySwtichIDByState.as_view()),
	# PORTS BY IP ADDR
	url(r'^port/ip/(?P<post_id>\w+)$', views.PortByIPAddr.as_view()),
	# VLAN
	url('vlan', views.VLANView.as_view()),
	# VLAN BY ID
	url(r'vlan/id/(?P<post_id>\w+)$', views.VLANByID.as_view()),
	# VLAN BY PORT
	url(r'vlan/port/(?P<post_id>\w+)$', views.VLANByPort.as_view()),
	# VLAN BY PORT BY SWITCH ID
	url(r'^vlan/port/(?P<post_id>\w+)/switch/(?P<post_id2>\w+)$', views.VLANByPortBySwitchID.as_view()),
	# ACL
	url('acl', views.ACLView.as_view()),
	# ACL BY ID
	url(r'acl/id/(?P<post_id>\w+)$', views.ACLByID.as_view()),
	# ACL BY USRNAME
	url(r'acl/email/(?P<post_id>\w+)$', views.ACLByEmail.as_view()),
	# AUDIT
	url('audit_log', views.Audit_LogView.as_view()),
	# AUDIT BY ID
	url(r'audit/id/(?P<post_id>\w+)$', views.Audit_LogByID.as_view()),
	# AUDIT BY ID
	url(r'audit/email/(?P<post_id>\w+)$', views.Audit_LogByEmail.as_view()),

]
