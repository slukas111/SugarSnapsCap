from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from users.models import Profile
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
    context = {
        'user': profile.user
        }
    return render(request, html, context)