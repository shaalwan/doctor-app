#models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
from datetime import datetime as dt

class Hospital(models.Model):
    name = models.CharField(max_length=500, default='')
    address = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=500, default='')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=10, blank=True, default='')
    address = models.CharField(max_length=128, blank=True, default='')
    email = models.EmailField(blank=False, null=False)
    image = models.ImageField(
        upload_to='profile_images/', default='profile_images/default.png', null=False)
    age = models.IntegerField(default=18, null=True)
    state = models.CharField(default='punjab',max_length=450)
    gender = models.CharField(default='male',max_length=100)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    token = models.TextField(null=True,blank=True)

class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Problem(models.Model):
    problem = models.CharField(max_length=5000)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.problem

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.user.username

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    data = models.TextField()

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    details = models.JSONField()
    date = models.DateField(auto_now_add=True)

class Xray(models.Model):
    pic_id = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='Xrays/', null=True)
    time = models.TimeField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    report = models.ForeignKey(Report, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.pic_id

class Appointment(models.Model):
    date = models.DateField(blank=True)
    time = models.TimeField(default = dt.now)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    #confirmed = 0 , cancled = 1, denied = 2 

class Notification(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciever')
    data = models.TextField()
    time = models.DateTimeField(auto_now=True)
    icon = models.IntegerField(default=1)# 1:askappointment 2:share 3:deny 4:accept
    status = models.IntegerField(default=0)# 1:seen 0:notseen
    



