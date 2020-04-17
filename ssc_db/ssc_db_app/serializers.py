from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user', 'department')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('code', 'name')

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = ('identifier', 'model', 'department')

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('number', 'ip_addr', 'state', 'switch')

class VLANSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLAN
        fields = ('identifier', 'description', 'port')

class ACLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACL
        fields = ('id', 'access_flag', 'user')

class Audit_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Log
        fields = ('id', 'action', 'user')
