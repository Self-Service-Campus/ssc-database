from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Switch)
admin.site.register(Port)
admin.site.register(VLAN)
admin.site.register(ACL)
admin.site.register(Audit_Log)
