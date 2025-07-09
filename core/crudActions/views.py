from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import BaseSuccessUrlMixin


class GenericCreateView(LoginRequiredMixin, BaseSuccessUrlMixin, CreateView):
    template_name = 'actions/generic_list.html'


class GenericUpdateView(LoginRequiredMixin, BaseSuccessUrlMixin, UpdateView):
    template_name = 'actions/generic_list.html'


class GenericDeleteView(LoginRequiredMixin, BaseSuccessUrlMixin, DeleteView):
    template_name = 'actions/generic_confirm_delete.html'



class GenericListView(LoginRequiredMixin, ListView):
    template_name = 'actions/generic_list.html'
    #model = None


class GenericDetailView(LoginRequiredMixin, DetailView):
    template_name = 'actions/generic_detail.html'



class GroupRequiredMixin(UserPassesTestMixin):
    group_required = None

    def test_func(self):
        return self.group_required and self.request.user.groups.filter(name=self.group_required).exists()


class FilterableListView(ListView):
    search_fields = []  # override in child class

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q and self.search_fields:
            from django.db.models import Q
            conditions = Q()
            for field in self.search_fields:
                conditions |= Q(**{f"{field}__icontains": q})
            queryset = queryset.filter(conditions)
        return queryset


class GenericUpdateView(UpdateView):
    template_name = 'actions/generic_list.html'
    def get_success_url(self):
        return (
                self.request.GET.get('next')
                or (self.object.get_absolute_url() if hasattr(self.object, 'get_absolute_url') else reverse('home'))
        )
