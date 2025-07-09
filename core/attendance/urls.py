from django.urls import path
from crudActions.views import GenericListView, GenericCreateView, GenericUpdateView, GenericDeleteView
from .models import AttendanceRecord

urlpatterns = [
    #path('', GenericListView.as_view(model=AttendanceRecord,template_name='attendance/attendance_list.html'), name='attendance-list'),
    path('attendance/', GenericListView.as_view(model=AttendanceRecord), name='attendance-list'),
    path('add/', GenericCreateView.as_view(model=AttendanceRecord, fields='__all__'), name='Attendance-create'),
    path('<int:pk>/edit/', GenericUpdateView.as_view(model=AttendanceRecord, fields='__all__'), name='Attendance-edit'),
    path('<int:pk>/delete/', GenericDeleteView.as_view(model=AttendanceRecord), name='Attendance-delete'),
]