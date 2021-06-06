from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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

    # home screen doctor
    path('patients', patientList.as_view({'get': 'list'}), name='patients-list'),
    #home screen patient + patient details doctor
    path('reports/<int:pk>',ReportList.as_view({'get':'list'}),name = 'report-list'),
    path('prescriptions/<int:pk>',PrescriptionList.as_view({'get':'list'}), name='prescription-list'),
    path('xrays/<int:pk>',XrayList.as_view({'get':'list'}),name = 'xray-list'),

    path('report/<int:pk>',ReportViewset.as_view(),name='patient-report'),
    path('xray/<int:pk>',XrayViewset.as_view(),name = 'patient-xray'),
    
    path('report/add',newReportViewset.as_view(),name='new-report'),
    path('xray/add',newXrayViewset.as_view(),name='new-Xray'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
