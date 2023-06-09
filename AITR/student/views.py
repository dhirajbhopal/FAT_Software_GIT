from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render , redirect
from django.http import HttpResponse
from student.models import fat
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

def insert(request):
    return render(request,'insert.html')

def all(request):
    fatall=fat.objects.all()
    return render(request,'fatall.html',{'fatall':fatall})

def rawall(request):
    rawall=fat.objects.all()
    return render(request,'rawall.html',{'rawall':rawall})

def insertqr(request):
    return render(request,'qrupdate.html')

def upload(req):
    fatdata=fat.objects.filter(status="raw")
    return render(req,'fatformat.html',{'fatdata':fatdata})

def new(request):
    fatdone=fat.objects.filter(status="raw")
    return render(request,'fatfinal.html',{'fatdone':fatdone})

def empfatdata(request):
    ob=fat()
    ob.name=request.POST.get("name")
    ob.empid=request.POST.get("empid")
    ob.dept=request.POST.get("dept")
    ob.circle=request.POST.get("circle")
    ob.location=request.POST.get("location")
    ob.grade=request.POST.get("grade")
    ob.date=request.POST.get("date")
    ob.certno=request.POST.get("certno")
    ob.image=request.FILES['image']
    ob.save()
    return HttpResponse("Data Saved")

def updateqr(req):
    certno=req.POST.get("certno")
    nqr=fat.objects.get(certno=certno)
    nqr.status="Done"
    nqr.qr=req.FILES['qr']
    nqr.save()
    return HttpResponse("New QR Code Updated")