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
        fields = ('name_dep', 'acron_dep')

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = ('identifier_switch', 'model_switch', 'department')

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('number_port', 'ip_addr_port', 'state_port', 'switch')

class VLANSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLAN
        fields = ('identifier_vlan', 'description_vlan', 'port')

class ACLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACL
        fields = ('id_acl', 'access_flag_acl', 'user')

class Audit_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Log
        fields = ('id_audit', 'action_audit', 'user')
