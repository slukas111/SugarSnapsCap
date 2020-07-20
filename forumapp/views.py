from django.shortcuts import redirect, render, get_object_or_404
from .forms import ForumPostForm, CommentForm
from .models import ForumPost, Comment
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ForumView(LoginRequiredMixin, CreateView):
    model = ForumPost
    fields = ['title', 'text']

    form_post = ForumPostForm
    form_comment = CommentForm

    def get(self, request):
        form = self.form_post()
        posts = ForumPost.objects.all().order_by('-id')
        return render(request, 'forumapp/forumpost.html', {'posts': posts, 'form': form})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class PostDetails(CreateView):
#     model = Comment
#     fields = ['text']
#
#     form_comment = CommentForm
#
#     def get(self, request, slug):
#         form = self.form_comment()
#         post = get_object_or_404(ForumPost, slug=slug)
#         return render(request, 'forumapp/post.html', {'post': post, 'form': form})
#
#     def form_valid(self, form):
#         post = get_object_or_404(ForumPost, id=postid)
#         form.instance.author = self.request.user
#         form.instance.forumPost = post
#         return super().form_valid(form)

#
@login_required()
def postdetails(request, slug):
    html = 'forumapp/post.html'
    post = get_object_or_404(ForumPost, slug=slug)
    allcomments = Comment.objects.filter(forumPost=post).order_by('-id')
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or NONE)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(
                author=request.user,
                forumPost=post,
                text=text
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, html, {
        'post': post,
        'allcomments': allcomments,
        'comment_form': comment_form
    })
