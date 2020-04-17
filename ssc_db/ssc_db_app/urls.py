from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('department', views.DepartmentView)
router.register('switch', views.SwitchView)
router.register('port', views.PortView)
router.register('vlan', views.VLANView)
router.register('acl', views.ACLView)
router.register('audit_log', views.Audit_LogView)


urlpatterns = [
    path('', views.index, name='index'),

    # AUTH VIEWS
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # ROUTER VIEWS
    path('', include(router.urls))
]
