#urls
from django.urls import path

from .views import *

urlpatterns = [
    #register and login
    path('register/doctor', registerDoctor.as_view(), name='doctor-signup'),
    path('register/patient', registerPatient.as_view(), name='patient-signup'),
    path('registerp',Registerp.as_view(),name='patient-register'),
    path('login', login.as_view(), name='login'),


    # users
    path('doctor/<int:pk>', doctorViewset.as_view(), name='doctor'),
    path('patient/<int:pk>', patientViewset.as_view(), name='patient'),
    path('user/<int:pk>', userViewset.as_view(), name='user'),
    path('doctors',DoctorList.as_view({'get':'list'}),name='doctorslist'),

    # home screen doctor
    path('problems',ProblemList.as_view({'get':'list'}),name = 'problem-list'),
    path('patients', patientList.as_view({'get': 'list'}), name='patients-list'),
    #home screen patient + patient details doctor
    path('reports/<int:pk>',ReportList.as_view({'get':'list'}),name = 'report-list'),
    path('prescriptions/<int:pk>',PrescriptionList.as_view({'get':'list'}), name='prescription-list'),
    path('xrays/<int:pk>',XrayList.as_view({'get':'list'}),name = 'xray-list'),
    path('appointments/<int:pk>',AppointmentList.as_view({'get':'list'}),name = 'Appointment-list'),

    path('report/<int:pk>',ReportViewset.as_view(),name='patient-report'),
    path('xray/<int:pk>',XrayViewset.as_view(),name = 'patient-xray'),
    path('prescription/<int:pk>',PrescriptionViewset.as_view(),name='patient-prescription'),
    
    path('report/add',newReportViewset.as_view(),name='new-report'),
    path('xray/add',newXrayViewset.as_view(),name='new-Xray'),
    path('prescription/add',newPrescriptionViewset.as_view(),name='new-prescription'),

    path('getappointment',AppointmentViewset.as_view(),name='new appointment'),

    #notifications
    path('askappointment',AskAppointment.as_view(),name='askappointment'),
    path('shareReport',Share.as_view(),name='shareReport'),
    path('notifications',NotificationList.as_view({'get':'list'}),name='notifications'),
    path('denyrequest',DenyAppointment.as_view(),name='deny request'),

    path('problem/add',newProblem.as_view(),name='add problem'),#test
    path('notification/<int:pk>',NotificationViewset.as_view(),name='notification get,edit'),
]
