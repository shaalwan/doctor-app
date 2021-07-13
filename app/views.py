from django.http import response
from django.http.response import Http404  # for bad request
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView  # view set to send data in api form
# used to return response of a API class
from rest_framework.response import Response
from rest_framework import status  # for response status
from rest_framework import viewsets  # for viewsets.read-only viewsets
# authenticating a user using username and password
from django.contrib.auth import authenticate
# to add filters in a readonly viewset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters  # to add search filter in readonly viewset

from .models import *
from .serializers import *
from .paginators import *


#login and register

class registerDoctor(APIView):

    def post(self, request, format=None):
        data = request.data  # getting data from body
        username = data['username']
        email = data['email']
        password = data['password']
        phone_number = data['contact']
        department = data['department']  # id of department

        user = User.objects.create_user(username, email, password)
        user.is_doctor = True  # making this them a doctor
        user.phone_number = phone_number
        user.save()
        departmentObj = Department.objects.get(pk=department)
        doctor = Doctor(user=user, department=departmentObj)
        doctor.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class registerPatient(APIView):

    def post(self, request, format=None):
        data = request.data  # getting data from body
        username = data['username']
        email = data['email']
        password = data['password']
        phone_number = data['contact']
        doctor = data['doctor']  # id of doctor

        user = User.objects.create_user(username, email, password)
        user.is_patient = True
        user.phone_number = phone_number
        user.save()
        doctorObj = Doctor.objects.get(pk=doctor)
        patient = Patient(user=user, doctor=doctorObj)
        patient.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class login(APIView):

    def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({"Error": "invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# user view,edit,delete


class doctorViewset(APIView):

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, requests, pk):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, requests, pk):
        doctor = self.get_object(pk)
        serializer = AddDoctor(doctor, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class patientViewset(APIView):

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, requests, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, requests, pk):
        patient = self.get_object(pk)
        serializer = AddPatient(patient, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userViewset(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, requests, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, requests, pk):
        user = self.get_object(pk)
        serializer = AddUser(user, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorList(viewsets.ReadOnlyModelViewSet):
    model = Doctor
    serializer_class = DoctorSerializer

    def get_queryset(self):
        doctors = Doctor.objects.filter(department__hospital=1)
        return doctors

# home pages
class ProblemList(viewsets.ReadOnlyModelViewSet):
    model = Problem
    serializer_class = ProblemSerializer
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        Problems = Problem.objects.filter(Department=1)
        return Problems


class patientList(viewsets.ReadOnlyModelViewSet):
    model = Patient
    serializer_class = PatientSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['problem']

    def get_queryset(self):
        patients = Patient.objects.filter(doctor=Doctor.objects.get(
            user=self.request.user)).order_by('user')
        return patients


class ReportList(viewsets.ReadOnlyModelViewSet):
    model = Report
    serializer_class = ReportSerializer
    #pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        reports = Report.objects.filter(
            patient=self.kwargs['pk']).order_by('-date')
        return reports


class PrescriptionList(viewsets.ReadOnlyModelViewSet):
    model = Prescription
    serializer_class = PrescriptionSerializer
    #pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        Prescriptions = Prescription.objects.filter(
            patient=self.kwargs['pk']).order_by('-date')
        return Prescriptions


class XrayList(viewsets.ReadOnlyModelViewSet):
    model = Xray
    serializer_class = XraySerializer
    #pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        xrays = Xray.objects.filter(
            patient=self.kwargs['pk']).order_by('-report__date')
        return xrays


class XrayViewset(APIView):
    def get_object(self, pk):
        try:
            return Xray.objects.get(pk=pk)
        except Xray.DoesNotExist:
            raise Http404

    def get(self, requests, pk):
        xray = self.get_object(pk)
        serializer = XraySerializer(xray)
        return Response(serializer.data)

    def put(self, requests, pk):
        xray = self.get_object(pk)
        serializer = addXray(xray, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests, pk):
        xray = self.get_object(pk)
        xray.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class newXrayViewset(APIView):
    def post(self, requests):
        serializer = addXray(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportViewset(APIView):
    def get_object(self, pk):
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist():
            raise Http404

    def get(self, requests, pk):
        report = self.get_object(pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, requests, pk):
        report = self.get_object(pk)
        serializer = ReportSerializer(report, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests, pk):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class newReportViewset(APIView):
    def post(self, requests):
        serializer = ReportSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class newAppointment(APIView):
    def post(self, requests):
        date = requests.data['date']
        patient = requests.data['patient']
        doctor = requests.user
        data = {"date": date, "patient": patient, "doctor": doctor}
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requests):
        appointment = Appointment.objects.get(
            date=requests.data['date'], patient=requests.data['patient'])
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


