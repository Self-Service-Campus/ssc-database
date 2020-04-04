from django.db import models

# Create your models here.
class Department(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"Departamento nº{code}: {name}"

class User(models.Model):
    uu = models.CharField(max_length=100, primary_key=True)
    email_ua = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.OneToOneField(Department, on_delete=models.CASCADE) # tenho de adicionar alguma coisa on_delete?
    
    def __str__(self):
        return f"User {uu}, @: {email_ua}, {first_name} {last_name}, dep: {department}"

class Switch(models.Model):
    identifier = models.CharField(max_length=100, primary_key=True)
    model = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Switch {identifier}, {model}, dep: {department}"


class Port(models.Model):
    number = models.IntegerField(primary_key=True)
    ip_addr = models.GenericIPAddressField()
    state = models.CharField(max_length=100)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"Port {number}, ip: {ip_addr}, state: {state}, from: {switch}"


class VLAN(models.Model):
    identifier = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=350)
    port = models.ForeignKey(Port, on_delete=models.CASCADE) # on_delete?

    def __str__(self):
        return f"VLAN {identifier}, {description}, port: {port}"


class ACL(models.Model):
    id = models.AutoField(primary_key=True)
    access_flag = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"ACL {id}, ip: {access_flag}, user: {user}"

class Audit_Log(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=350)

    def __str__(self):
        return f"Audit {id}: {action}"