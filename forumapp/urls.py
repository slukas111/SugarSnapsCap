from django.urls import path
from .views import ForumView, postdetails

urlpatterns = [
    path('forum/', ForumView.as_view(), name='forum'),
    path('post_details/<str:slug>/', postdetails, name='forumpostdetails'),
]
