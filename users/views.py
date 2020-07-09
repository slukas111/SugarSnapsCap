from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from users.models import Profile
from sugar_app.models import BoxItem
from users.forms import EditProfileForm

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
        'donations': donations,
        'id': profile.id,
        'bio': profile.bio    
        }
    return render(request, html, context)

def EditUser(request, id):
    user = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.bio = data['bio']
            user.profile_image = data['profile_image']
            user.save()
            return HttpResponseRedirect(reverse('user_profile', args=(id, )))
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
