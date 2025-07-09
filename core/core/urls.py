"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface

    # Attendance app URLs
    path('', include('attendance.urls')),

    # Classes app URLs
    #path('classes/', include('classes.urls')),

    # Communication app URLs
    #path('communication/', include('communication.urls')),

    # Events app URLs
   # path('events/', include('events.urls')),

    # Finance app URLs
    #path('finance/', include('finance.urls')),

    # Grades app URLs
    #path('grades/', include('grades.urls')),

    # Library app URLs
    #path('library/', include('library.urls')),

    # Reports app URLs
    #path('reports/', include('reports.urls')),

    # Students app URLs
    path('', include('students.urls')),

    # Teachers app URLs
    #path('teachers/', include('teachers.urls')),

    # Users app URLs
    #path('users/', include('users.urls')),

    # Mainpoint app URLs - set as the root (home/landing) page
    path('', include('mainpoint.urls')),
    path('crudActions/',include('crudActions.urls')),
]