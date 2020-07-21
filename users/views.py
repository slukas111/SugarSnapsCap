from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import Profile
from sugar_app.models import BoxItem
from users.forms import EditProfileForm
from notifications.signals import notify

# new

from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(
                request, f'Your accout has been created! Now you can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_profile_view(request, user_id):
    html = 'user_profile.html'
    profile = User.objects.get(id=user_id).profile
    user = User.objects.get(id=user_id)
    reserve_box = BoxItem.objects.all()
    donations = BoxItem.objects.filter(profile=user_id).order_by('-id')
    all_followers = request.user.profile.following.all()
    following_count = all_followers.count()
    notification = user.notifications.read()
    noti = user.notifications.unread()
    context = {
        'donations': donations,
        'id': profile.id,
        'bio': Profile.objects.get(user=user).bio,
        'all_followers': all_followers,
        'following_count': following_count,
        'profile': profile,
        'is_following': profile in all_followers,
        'user': user,
        'image': profile.profile_image,
        'noti': noti,
        'notification': notification,
        'reserve_box':reserve_box
    }
    return render(request, html, context)


def editUser(request, id):
    user = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data = form.cleaned_data
            user.bio = data['bio']
            user.profile_image = data['profile_image']
            user.save()
            return HttpResponseRedirect(reverse('user_profile', args=(id,)))

    form = EditProfileForm(initial={
        'bio': user.bio,
        'profile_image': user.profile_image
    })
    return render(request, 'editUser.html', {'form': form})


class UserPostListView(ListView):
    model = BoxItem
    template_name = 'user_profile.html'
    context_object_name = 'donations'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BoxItem.objects.filter(profile=user).order_by('-date_posted')


@login_required
def Follow(request, id):
    html = "user_profile.html"
    own_profile = request.user.profile  # or your queryset to get
    following_profile = Profile.objects.get(id=id)
    own_profile.following.add(following_profile)  # and .remove() for unfollow
    own_profile.save()
    message = 'started to following you.'
    notify.send(sender=own_profile, recipient=following_profile.user, verb=message, description=own_profile.user.id)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def Unfollow(request, id):
    html = "user_profile.html"
    own_profile = request.user.profile  # or your queryset to get
    following_profile = Profile.objects.get(id=id)
    own_profile.following.remove(following_profile)  # and .remove() for unfollow
    own_profile.save()
    notify.send(sender=own_profile, recipient=following_profile.user, verb='unfollowed you.',
                description=own_profile.user.id)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
