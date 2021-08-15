from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Problem)
admin.site.register(Patient)
admin.site.register(Report)
admin.site.register(Prescription)
admin.site.register(Xray)
admin.site.register(Appointment)
admin.site.register(Notification)
