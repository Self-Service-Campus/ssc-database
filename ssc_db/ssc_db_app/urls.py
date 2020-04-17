from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers
from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="SSC API DOCUMENTATION")

router = routers.DefaultRouter()
# USER
router.register('user', views.UserView)
# USER BY DEPARTMENT CODE
router.register(r'^user/dep/(?P<post_id>\w+)$', views.UserByDepartmentAcron)

# DEPARTMENT
router.register('department', views.DepartmentView)
# DEPARTMENT BY CODE
router.register(r'^department/(?P<post_id>\w+)$', views.DepartmentByAcron)

# SWITCH
router.register('switch', views.SwitchView)
# SWITCH BY CODE
router.register(r'^switch/code/(?P<post_id>\w+)$', views.SwitchByIdentifier)
# SWITCHES BY MODEL
router.register(r'^switch/model/(?P<post_id>\w+)$', views.SwitchsByModel)
# SWITCHES BY DEPARTMENT CODE
router.register(r'^switch/dep/(?P<post_id>\w+)$', views.SwitchsByDepartmentAcron)

# PORTS
router.register('port', views.PortView)
# PORTS BY SWITCH IDENTIFIER
router.register(r'^port/switch/(?P<post_id>\w+)$', views.PortBySwitchID)
# PORTS BY STATE BY SWITCH ID
router.register(r'^port/switch/(?P<post_id>\w+)/state/(?P<post_id2>\w+)$', views.PortBySwtichIDByState)
# PORTS BY IP ADDR
router.register(r'^port/ip/(?P<post_id>\w+)$', views.PortByIPAddr)

# VLAN
router.register('vlan', views.VLANView)
# VLAN BY ID
router.register(r'vlan/id/(?P<post_id>\w+)$', views.VLANByID)
# VLAN BY PORT
router.register(r'vlan/port/(?P<post_id>\w+)$', views.VLANByPort)
# VLAN BY PORT BY SWITCH ID
router.register(r'^vlan/port/(?P<post_id>\w+)/switch/(?P<post_id2>\w+)$', views.VLANByPortBySwitchID)

# ACL
router.register('acl', views.ACLView)
# ACL BY ID
router.register(r'acl/id/(?P<post_id>\w+)$', views.ACLByID)
# ACL BY USRNAME
router.register(r'acl/email/(?P<post_id>\w+)$', views.ACLByEmail)

# AUDIT
router.register('audit_log', views.Audit_LogView)
# AUDIT BY ID
router.register(r'audit/id/(?P<post_id>\w+)$', views.Audit_LogByID)
# AUDIT BY ID
router.register(r'audit/email/(?P<post_id>\w+)$', views.Audit_LogByEmail)





urlpatterns = [
    path('', views.index, name='index'),

    # AUTH VIEWS
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # ROUTER VIEWS
    path('', include(router.urls)),

    path('api_doc/', schema_view)

]
