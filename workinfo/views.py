from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import EmployeePersonal,EmployeeQualify,EmployeeWork
# Create your views here.

def index(request):
    if request.method == "POST":
        print(request)
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        age = request.POST.get('age','')
        print(fname, lname, age)
        empPersonal = EmployeePersonal(fname = fname, lname = lname, age = age)
        empPersonal.save()
    return render(request, 'personalDetails.html')

def empwork(request):
    if request.method == "POST":
        cname = request.POST.get('cname','')
        empPersonal = EmployeeWork(cname = cname)
        empPersonal.save() 
    return render(request,'workDetails.html')

def qualify(request):
    if request.method == "POST":
        uname = request.POST.get('uname','')
        empPersonal = EmployeeQualify(uname = uname)
        empPersonal.save() 
    return render(request, 'qualification.html')

def finish(request):
    return render(request, 'finish.html')