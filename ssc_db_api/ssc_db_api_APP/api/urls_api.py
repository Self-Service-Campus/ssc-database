from django.conf.urls import url
from django.urls import path, include
from .views_api import *

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="SSC API DOCUMENTATION")

urlpatterns = [
	# SWAGGER
	path('api_doc/', schema_view),

	# --- API ENDPOINTS ---
	# --- USER ---
	url('user', UserView.as_view()),
	# USER BY DEPARTMENT ACRON
	url(r'^user/dep/(?P<post_id>\w+)$', UserByDepartmentAcron.as_view()),

	# --- DEPARTMENT ---
	url('dep', DepartmentView.as_view()),
	# DEPARTMENT BY ACRON
	url(r'^dep/(?P<post_id>\w+)$', DepartmentByAcron.as_view()),

	# --- SWITCH ---
	url('switch', SwitchView.as_view()),
	# SWITCH BY ID_SWITCH
	url(r'^switch/id/(?P<post_id>\w+)$', SwitchById.as_view()),
	# SWITCHES BY MODEL
	url(r'^switch/model/(?P<post_id>\w+)$', SwitchsByModel.as_view()),
	# SWITCHES BY DEPARTMENT CODE
	url(r'^switch/dep/(?P<post_id>\w+)$', SwitchsByDepartmentAcron.as_view()),

	# --- PORT ---
	url('port', PortView.as_view()),
	# PORT BY ID
	url(r'^port/id/(?P<post_id>\w+)$', PortById.as_view()),
	# PORTS BY SWITCH ID
	url(r'^port/switch/id/(?P<post_id>\w+)$', PortBySwitchID.as_view()),
	# PORTS BY STATE BY SWITCH ID
	url(r'^port/switch/id/(?P<post_id>\w+)/state/(?P<post_id2>\w+)$', PortBySwtichIDByState.as_view()),

	# --- VLAN ---
	url('vlan', VLANView.as_view()),
	# VLAN BY ID
	url(r'vlan/id/(?P<post_id>\w+)$', VLANByID.as_view()),
	# VLAN BY PORT ID
	url(r'vlan/port/id/(?P<post_id>\w+)$', VLANByPortID.as_view()),
	# VLAN BY PORT NUMBER BY SWITCH ID
	url(r'^vlan/port/(?P<post_id>\w+)/switch/(?P<post_id2>\w+)$', VLANByPortNumberBySwitchID.as_view()),

	# --- ACL ---
	url('acl', ACLView.as_view()),
	# ACL BY ID
	url(r'acl/id/(?P<post_id>\w+)$', ACLByID.as_view()),
	# ACL BY USRNAME
	url(r'acl/email/(?P<post_id>\w+)$', ACLByEmail.as_view()),

	# --- AUDIT ---
	url('audit_log', Audit_LogView.as_view()),
	# AUDIT BY ID
	url(r'audit/id/(?P<post_id>\w+)$', Audit_LogByID.as_view()),
	# AUDIT BY EMAIL
	url(r'audit/email/(?P<post_id>\w+)$', Audit_LogByEmail.as_view()),

]
