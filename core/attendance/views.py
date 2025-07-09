from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import AttendanceRecord
from core.crudActions.mixins import BaseSuccessUrlMixin


"""# Create your views here.
class GenericCreateView(LoginRequiredMixin, BaseSuccessUrlMixin, CreateView):
    model = AttendanceRecord
    template_name = 'attendance/generic_form.html'
    
    
class GenericCreateView(LoginRequiredMixin, BaseSuccessUrlMixin, CreateView):
    model = AttendanceRecord
    template_name = 'attendance/generic_form.html'"""

class GenericListView(LoginRequiredMixin, ListView):
    model = AttendanceRecord
    #template_name = 'attendance/attendancerecord_list.html'
    #model = None