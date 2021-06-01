from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE



class Hospital(models.Model):
    name = models.CharField(max_length=500,default='')
    address = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=500,default='')
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=10,blank= True, default='')
    address = models.CharField(max_length=128,blank= True, default='')
    email = models.EmailField(blank=False,null=False)
    image = models.ImageField(upload_to='profile_images/',default='profile_images/default.png',null =False)
    age = models.IntegerField(default=18,null=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    problem = models.CharField(max_length=500)
    def __str__(self):
        return self.user.username

class Report(models.Model):
    patient = models.ForeignKey(Patient,on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)
    data = models.TextField()

class Prescription(models.Model):
    patient = models.ForeignKey(Patient,on_delete=CASCADE)
    details = models.JSONField()
    date = models.DateField(auto_now_add=True)






























