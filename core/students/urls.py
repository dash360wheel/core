from django.urls import path
from crudActions.views import GenericListView, GenericCreateView, GenericUpdateView, GenericDeleteView
from .models import Student

urlpatterns = [
    path('students/', GenericListView.as_view(model=Student), name='student-list'),
    path('add/', GenericCreateView.as_view(model=Student, fields='__all__'), name='student-create'),
    path('<int:pk>/edit/', GenericUpdateView.as_view(model=Student, fields='__all__'), name='student-edit'),
    path('<int:pk>/delete/', GenericDeleteView.as_view(model=Student), name='student-delete'),
]
