from django.urls import path
from .views import *

urlpatterns = [
    #register and login
    path('register/doctor', registerDoctor.as_view(), name='doctor-signup'),
    path('register/patient', registerPatient.as_view(), name='patient-signup'),
    path('login', login.as_view(), name='login'),


    # users
    path('doctor/<int:pk>', doctorViewset.as_view(), name='doctor'),
    path('patient/<int:pk>', patientViewset.as_view(), name='patient'),
    path('user/<int:pk>', userViewset.as_view(), name='user'),

    # home screen
    path('patients', patientList.as_view({'get': 'list'}), name='patients-list'),
    path('reports/<int:pk>',ReportList.as_view({'get':'list'}),name = 'report-list'),
    path('prescriptions/<int:pk>',PrescriptionList.as_view({'get':'list'}), name='prescription-list'),
]
