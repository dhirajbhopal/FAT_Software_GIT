from django.db import models
import os
import datetime
# Create your models here.

def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)

   
class fat(models.Model):
	name=models.CharField(max_length=15,null=False)
	empid=models.CharField(max_length=15,null=False)
	dept=models.CharField(max_length=15,null=False)
	circle=models.CharField(max_length=15,null=False)
	location=models.CharField(max_length=40,null=False)
	grade=models.CharField(max_length=100,null=False)
	date=models.CharField(max_length=15,null=False)
	certno=models.CharField(max_length=15,null=False)
	image=models.ImageField(upload_to=filepath,null=True,blank=True)
	qr=models.ImageField(upload_to=filepath,null=True,blank=True)
	status=models.CharField(max_length=15,null=True,default="raw")

def __str__(self):
	return self.name