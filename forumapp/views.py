from django.shortcuts import redirect, render, get_object_or_404
from .forms import ForumPostForm, CommentForm
from .models import ForumPost, Comment
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ViewForumPostList(ListView):
    model = ForumPost
    template_name = 'forumapp/forumpost.html'
    context_object_name = 'posts'
