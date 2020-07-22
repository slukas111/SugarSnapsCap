from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .donation_form import AddBoxItemForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DatePickerInput
from .models import BoxItem, Categories
from django.views.defaults import page_not_found
from notifications.signals import notify
from users.models import Profile


# Create your views here.
class PostListView(ListView):
    model = BoxItem
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        # context['posts'] = BoxItem.objects.all().order_by('-id')
        return context

    def get_queryset(self):
        category = self.request.GET.get('filter')
        category_dict = Categories.objects.all().values()
        category_list = [category['category'] for category in category_dict]
        if category in category_list:
            category_item = category_list.index(category) + 1
            return BoxItem.objects.filter(item_category=category_item)
        return BoxItem.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BoxItem
    fields = ['title', 'item_category', 'description',
              'que_assign', 'expiration', 'image']

    def get_form(self):
        curr_user = self.request.user
        print('current user', curr_user)
        form = super().get_form()
        form.fields['expiration'].widget = DatePickerInput()
        notify.send(sender=self.request.user,
                    recipient=self.request.user, verb='donation posted')
        return form

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = BoxItem


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BoxItem
    fields = ['title', 'item_category', 'description',
              'expiration', 'que_assign', 'image']

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


@login_required()
def reserve(request, slug):
    box_item = BoxItem.objects.get(slug=slug)
    action = box_item.slug
    own_profile = request.user.profile  # or your queryset to get
    box_item.reserve.add(own_profile)
    message = ' has reserved '
    notify.send(sender=own_profile, recipient=box_item.profile, verb=message, target=box_item, action=box_item,
                description=action)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def bad_request(request, exception):
    return page_not_found(request, exception, template_name="404.html")


def bad_request_500(request):
    return render(request, template_name="500.html")
