from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from users.models import Profile
from sugar_app.models import BoxItem

# Create your views here.


@login_required
def index(request):
    html = 'index.html'
    user = request.user
    context = {
        'user': user
    }
    return render(request, html, context)


def user_profile_view(request, user_id):
    html = 'user_profile.html'
    profile = Profile.objects.get(id=user_id)
    donations = BoxItem.objects.filter(profile=user_id).order_by('-id')
    context = {
        'user': profile.user,
        'donations': donations
        }
    return render(request, html, context)


class UserPostListView(ListView):
    model = BoxItem
    template_name = 'user_profile.html'
    context_object_name = 'donations'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BoxItem.objects.filter(profile=user).order_by('-date_posted')
