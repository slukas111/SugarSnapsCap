from django.urls import path, include
from users.views import user_profile_view, UserPostListView, editUser, Follow, Unfollow, deleteuser

urlpatterns = [
    path('profile/<int:user_id>/', user_profile_view, name='user_profile'),
    path('user/<str:username>/', UserPostListView.as_view(), name="userposts"),
    path('edit/<int:id>/', editUser, name='updateprofile'),
    path('follow/<int:id>/', Follow, name="follow"),
    path('unfollow/<int:id>/', Unfollow, name="unfollow"),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('users/delete/', deleteuser , name='deleteuser')

]
