from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers
from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="SSC API DOCUMENTATION")

urlpatterns = [
    
    path('', views.index, name='index'),
        
    # DATABASE
    path('load_db/', views.load_database, name='load_db'),
    path('clean_db/', views.clean_database, name='clean_db'),

    # API URLS
    path('', include('ssc_db_api_APP.api.urls_api')),

    # AUTH VIEWS
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
