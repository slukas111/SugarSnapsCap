from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .donation_form import AddBoxItemForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BoxItem


# Create your views here.
# def index(request):
#     html = 'index.html'
#     posts = BoxItem.objects.all()
#     return render(request, html, {"posts": posts})


class PostListView(ListView):
    model = BoxItem
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    print('listview')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BoxItem
    fields = ['title', 'item_category', 'description', 'expiration', 'que_assign', 'image']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = BoxItem


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BoxItem
    fields = ['title', 'item_category', 'description', 'expiration', 'que_assign', 'image']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # get the post first
        if self.request.user == post.profile:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BoxItem
    success_url = '/'

    def test_func(self):
        post = self.get_object()  # get the post first
        if self.request.user == post.profile:
            return True
        return False


def reserve(request, slug):
    box_item = BoxItem.objects.get(slug=slug)
    print('box', box_item)
    own_profile = request.user.profile  # or your queryset to get
    box_item.reserve.add(own_profile)

    return HttpResponseRedirect("/")
