# actions/mixins.py

from django.urls import reverse_lazy
from django.shortcuts import resolve_url

class BaseSuccessUrlMixin:
    """
    A flexible success URL mixin that checks for:
    1. ?next=... in the request
    2. self.object.get_absolute_url() if it exists
    3. Fallback to default `success_url`
    """

    success_url = reverse_lazy('home')  # fallback if nothing else works

    def get_success_url(self):
        # 1. Check for ?next=
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        # 2. Check if object has get_absolute_url()
        if hasattr(self.object, 'get_absolute_url'):
            return resolve_url(self.object.get_absolute_url())

        # 3. Fallback
        return str(self.success_url)
