from django.shortcuts import render
from .donation_form import AddBoxItemForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BoxItem


# Create your views here.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BoxItem
    fields = ['title', 'item_category', 'description', 'expiration', 'que_assign', 'image']

    def get_form(self):
        form = super().get_form()
        form.instance.profile = self.request.user
        # form.fields['expiration'].widget = DateTimePickerInput()
        return form


class PostDetailView(DetailView):
    model = BoxItem


