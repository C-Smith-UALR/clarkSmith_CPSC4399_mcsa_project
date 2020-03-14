from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class McsaPhysician(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    maxShiftLoad = models.IntegerField(default=0)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.lastName

class McsaShift(models.Model):
    start_day = models.DateField('Day of shift start', help_text='Day of shift start')
    end_day = models.DateField('Day of shift end', help_text='Day of shift end')
    start_time = models.TimeField('Starting time', help_text='Starting time')
    end_time = models.TimeField('Ending time', help_text='Ending time')
    notes = models.TextField('Textual notes', help_text='Textual Notes', blank=True, null=True)
    service = models.CharField(max_length=30, default='Inpatient Center')
    physicianOnCall = models.ForeignKey(McsaPhysician, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # return self.physicianOnCall.lastName
        return self.service

