from django.urls import path, include
# from Adtaa import views as Adtaa_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from mcsa import views as mcsa_views


from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selectcal/', mcsa_views.monthYearAddView.as_view(template_name='mcsa/selectcal.html'), name='selectcal'),
    path('calendar/', mcsa_views.CalendarView.as_view(template_name='mcsa/calendar.html'), name='calendar'),
]