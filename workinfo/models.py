from django.db import models

# Create your models here.
class EmployeePersonal(models.Model):
    emp_id = models.AutoField
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)

    def __str__(self):  
        return self.fname

class EmployeeWork(models.Model):
    cname = models.CharField(max_length = 50)

    def __str__(self):  
        return self.cname

class EmployeeQualify(models.Model):
    uname = models.CharField(max_length=50)

    def __str__(self):
        return self.uname