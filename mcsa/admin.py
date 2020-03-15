from django.contrib import admin
from .models import McsaShift, McsaPhysician, userMonthYear

admin.site.register(McsaShift)
admin.site.register(McsaPhysician)
admin.site.register(userMonthYear)
