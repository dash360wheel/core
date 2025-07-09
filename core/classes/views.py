from django.shortcuts import render

# Create your views here.
from django.urls import path
from crudActions.views import KenericListView, GenericCreateView, GenericUpdateView, GenericDeleteView
from .models import Attendance

urlpatterns = [
    path('attendance/', KenericListView.as_view(model=Attendance), name='Attendance-list'),
    path('add/', GenericCreateView.as_view(model=Attendance, fields='__all__'), name='Attendance-create'),
    path('<int:pk>/edit/', GenericUpdateView.as_view(model=Attendance, fields='__all__'), name='Attendance-edit'),
    path('<int:pk>/delete/', GenericDeleteView.as_view(model=Attendance), name='Attendance-delete'),
]
