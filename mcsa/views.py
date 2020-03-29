from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import McsaShift, McsaPhysician, userMonthYear
# from Adtaa import auto_solutions_generator as coffeeFx
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime
# from .utils import render_to_pdf
from .utils import Calendar
from mcsa import schedulingAlgorithm as schedulerFx

def index(request):
    return render(request, 'mcsa/index.html')

class CalendarView(generic.ListView):
    model = McsaShift
    template_name = 'mcsa/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d=userMonthYear.objects.latest('pk')
        McsaShift.objects.all().delete()
        schedulerFx.main(d.userMonth, d.userYear)
        cal=Calendar(d.userYear, d.userMonth)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

class monthYearAddView(CreateView):
    model = userMonthYear
    fields = ['userMonth', 'userYear']
    # labels = {
    #     'userMonth': 'Month',
    #     'userYear': 'Year'
    # }