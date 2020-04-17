from django.db import models
from django.contrib.auth.models import User as usr

# Create your models here.
class Department(models.Model):

    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"Departamento nº{self.code}: {self.name}"

class User(models.Model):
    user = models.ForeignKey(usr, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE) # tenho de adicionar alguma coisa on_delete?

    def __str__(self):
        return f"User {self.user}, dep: {self.department}"

class Switch(models.Model):
    identifier = models.CharField(max_length=100, primary_key=True)
    model = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Switch {self.identifier}, {self.model}, dep: {self.department}"


class Port(models.Model):
    number = models.IntegerField(primary_key=True)
    ip_addr = models.GenericIPAddressField()
    state = models.CharField(max_length=100)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"Port {self.number}, ip: {self.ip_addr}, state: {self.state}, from: {self.switch}"


class VLAN(models.Model):
    identifier = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=350)
    port = models.ForeignKey(Port, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"VLAN {self.identifier}, {self.description}, port: {self.port}"


class ACL(models.Model):
    id = models.AutoField(primary_key=True)
    access_flag = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"ACL {self.id}, ip: {self.access_flag}, user: {self.user}"

class Audit_Log(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Audit {self.id}: {self.action}, by: {self.user}"