from django.db.models import fields
from django.db.models.query import prefetch_related_objects
from rest_framework import serializers
from rest_framework.compat import apply_markdown
from .models import *
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(max_length=10, write_only=True)
    is_doctor = serializers.BooleanField(default=0)
    is_patient = serializers.BooleanField(default=0)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone_number', 'is_doctor', 'is_patient']

class AddUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone_number', 'address', 'email', 'image', 'age']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['user', 'doctor', 'problem']

class AddPatient(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'department']

class AddDoctor(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class XraySerializer(serializers.ModelSerializer):
    report = ReportSerializer()
    class Meta:
        model = Xray
        fields = ['patient','pic_id','image','time','category','report']

class addXray(serializers.ModelSerializer):
    class Meta:
        model = Xray
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'