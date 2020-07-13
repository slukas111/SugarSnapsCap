from django import forms

from .models import ForumPost, Comment


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        exclude = ['author', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
