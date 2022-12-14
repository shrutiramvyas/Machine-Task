from django.contrib import admin
from .models import EmployeePersonal,EmployeeQualify,EmployeeWork


# Register your models here.
admin.site.register(EmployeePersonal)
admin.site.register(EmployeeQualify)
admin.site.register(EmployeeWork)