from django.shortcuts import render

# Create your views here.


# mainpoint/views.py
from django.views.generic import ListView
from .models import Announcement


class HomePageView(ListView):
    model = Announcement
    #template_name = 'mainpoint/home.html'  # extend base.html
    context_object_name = 'announcements'
