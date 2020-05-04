from django.db import models
from django.contrib.auth.models import User as usr

# https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

class Department(models.Model):
    acron_dep = models.CharField(primary_key=True, max_length=150, unique=True)
    name_dep = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.acron_dep} - {self.name_dep}"


class User(models.Model):
    user = models.ForeignKey(usr, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE) # tenho de adicionar alguma coisa on_delete?

    def __str__(self):
        return f"User {self.user}, dep: {self.department}"


class Switch(models.Model):
    id_switch = models.CharField(max_length=100, primary_key=True)
    ip_switch = models.CharField(max_length=100)
    model_switch = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Switch {self.id_switch}, model: {self.model_switch}, dep: {self.department}"


class Port(models.Model):
    id_port = models.CharField(primary_key=True, max_length=300)
    number_port = models.CharField(max_length=100)
    name_port = models.CharField(max_length=100)
    state_port = models.CharField(max_length=100)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"Port {self.id_port}, number: {self.number_port}, name: {self.name_port}, state: {self.state_port}, switch: {self.switch}"


class VLAN(models.Model):
    id_vlan = models.CharField(primary_key=True, max_length=300)
    description_vlan = models.CharField(max_length=350)
    # Port ou port__id?? a ver vamos
    port = models.ForeignKey(Port, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"VLAN {self.id_vlan}, description: {self.description_vlan}, port: {self.port}"


class ACL(models.Model):
    id_acl = models.AutoField(primary_key=True)
    access_flag_acl = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"ACL {self.id_acl}, flag: {self.access_flag_acl}, user: {self.user}"


class Audit_Log(models.Model):
    id_audit = models.AutoField(primary_key=True)
    action_audit = models.CharField(max_length=350) # Descreve oq aconteceu
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Audit {self.id_audit}: {self.action_audit}, by: {self.user}, date: {self.date}"