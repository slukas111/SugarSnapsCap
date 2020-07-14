from django.urls import path
from .views import  ViewForumPostList

urlpatterns = [
    path('test/', ViewForumPostList.as_view(), name='ViewForumPostList'),
]
