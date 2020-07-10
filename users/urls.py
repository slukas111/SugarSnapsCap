from django.urls import path
from users.views import index, user_profile_view, UserPostListView, EditUser, Follow, Unfollow

urlpatterns = [
    path('', index, name='homepage'),
    path('profile/<int:user_id>', user_profile_view, name='user_profile'),
    path('user/<str:username>/', UserPostListView.as_view(), name="userposts"),
    path('edit/<int:id>', EditUser),
    path('follow/<int:id>/', Follow, name="follow"),
    path('unfollow/<int:id>/', Unfollow, name="unfollow")

]
