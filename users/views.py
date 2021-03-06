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
from .forms import UserRegisterForm, UserDeleteForm

# Create your views here.


@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('login')
    else:
        delete_form = UserDeleteForm(instance=request.user)
    context = {
        'delete_form': delete_form
    }
    return render(request, 'users/delete_account.html', context)


def register(request):
    if request.user.is_authenticated():
        return redirect('homepage')
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
    logged_in_user = request.user
    profile = User.objects.get(id=user_id).profile
    user = User.objects.get(id=user_id)
    donations = BoxItem.objects.filter(profile=user_id).order_by('-id')
    all_followers = user.profile.following.all()
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
        'is_following': logged_in_user in all_followers,
        'user': user,
        'image': profile.profile_image,
        'noti': noti,
        'notification': notification
    }
    return render(request, html, context)


def editUser(request, id):
    user = Profile.objects.get(id=id)
    if request.user.id == user.id:
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
    return redirect('/')


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
    following_profile.following.add(own_profile)  # and .remove() for unfollow
    following_profile.save()
    message = 'started to following you.'
    notify.send(sender=own_profile, recipient=following_profile.user, verb=message, description=own_profile.user.id)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    


@login_required
def Unfollow(request, id):
    html = "user_profile.html"
    own_profile = request.user.profile  # or your queryset to get
    following_profile = Profile.objects.get(id=id)
    following_profile.following.remove(own_profile)  # and .remove() for unfollow
    following_profile.save()
    notify.send(sender=own_profile, recipient=following_profile.user, verb='unfollowed you.',
                description=own_profile.user.id)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
