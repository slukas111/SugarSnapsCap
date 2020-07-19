# from django.shortcuts import render, reverse, HttpResponseRedirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
#
# from .forms import LoginForm, SignUpForm
# from users.models import Profile
#
# # Create your views here.
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 username=data['username'],
#                 password=data['password']
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(
#                     request.GET.get('next', reverse('homepage'))
#                 )
#     form = LoginForm()
#     return render(request, 'login.html', {'form': form})
#
#
# @login_required
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('login'))
#
#
# def signup_view(request):
#     html = 'signup.html'
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             user.profile.email = form.cleaned_data.get('email')
#             user.profile.location = form.cleaned_data.get('location')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('homepage'))
#     else:
#         form = SignUpForm(instance)
#
#     form = SignUpForm()
#     context = {'form': form}
#     return render(request, html, context)
