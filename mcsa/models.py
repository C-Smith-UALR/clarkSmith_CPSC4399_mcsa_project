from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class McsaPhysician(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    maxShiftLoad = models.IntegerField(default=0)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.lastName

class McsaShift(models.Model):
    # start_day = models.DateField('Day of shift start', help_text='Day of shift start')
    # end_day = models.DateField('Day of shift end', help_text='Day of shift end')
    # start_time = models.TimeField('Starting time', help_text='Starting time')
    # end_time = models.TimeField('Ending time', help_text='Ending time')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    physicianOnCall = models.ForeignKey(McsaPhysician, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # return self.physicianOnCall.lastName
        return self.title

class userMonthYear(models.Model):
    MONTH_CHOICES = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    YEAR_CHOICES = (
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
    )

    userMonth=models.IntegerField(verbose_name="Month", choices=MONTH_CHOICES, default=1)
    userYear=models.IntegerField(verbose_name="Year", choices=YEAR_CHOICES, default=2020)

    def get_absolute_url(self):
        return reverse('calendar')