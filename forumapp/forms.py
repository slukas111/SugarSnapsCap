from django import forms

from .models import ForumPost, Comment


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        exclude = ['author', 'slug', 'created_on']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
