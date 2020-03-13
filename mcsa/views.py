from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Course, Instructor, ScheduledCourse
# from Adtaa import auto_solutions_generator as coffeeFx
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
# from .utils import render_to_pdf

def index(request):
    return render(request, 'mcsa/index.html')