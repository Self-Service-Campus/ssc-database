from django.db import models
from django.contrib.auth.models import User as usr


class Department(models.Model):

    id_dep = models.AutoField(primary_key=True)
    name_dep = models.CharField(max_length=150)
    acron_dep = models.CharField(max_length=150)

    def __str__(self):
        return f"Departamento {self.acron_dep}: {self.name_dep}, ID: {self.id_dep}"


class User(models.Model):
    user = models.ForeignKey(usr, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE) # tenho de adicionar alguma coisa on_delete?

    def __str__(self):
        return f"User {self.user}, dep: {self.department}"


class Switch(models.Model):
    identifier_switch = models.CharField(max_length=100, primary_key=True)
    model_switch = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Switch {self.identifier_switch}, {self.model_switch}, dep: {self.department}"


class Port(models.Model):
    id_port = models.AutoField(primary_key=True)
    number_port = models.IntegerField()
    ip_addr_port = models.GenericIPAddressField()
    state_port = models.CharField(max_length=100)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"Port {self.number_port}, ip: {self.ip_addr_port}, state: {self.state_port}, ID: {self.id_port}, from: {self.switch}"


class VLAN(models.Model):
    identifier_vlan = models.IntegerField(primary_key=True)
    description_vlan = models.CharField(max_length=350)
    # Port ou port__id?? a ver vamos
    port = models.ForeignKey(Port, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"VLAN {self.identifier_vlan}, {self.description_vlan}, port: {self.port}"


class ACL(models.Model):
    id_acl = models.AutoField(primary_key=True)
    access_flag_acl = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"ACL {self.id_acl}, ip: {self.access_flag_acl}, user: {self.user}"


class Audit_Log(models.Model):
    id_audit = models.AutoField(primary_key=True)
    action_audit = models.CharField(max_length=350) # Descreve oq aconteceu
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Audit {self.id_audit}: {self.action_audit}, by: {self.user}"