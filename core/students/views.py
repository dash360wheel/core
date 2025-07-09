from django.shortcuts import render
from core.crudActions.views import FilterableListView
from .models import Student


# Create your views here.
class StudentListView(FilterableListView):
    model = Student
    search_fields = ['first_name', 'last_name', 'email']
    template_name = 'actions/generic_list.html'
