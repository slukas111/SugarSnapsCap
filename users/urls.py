from django.urls import path
from users.views import index, user_profile_view, UserPostListView, EditUser

urlpatterns = [
    path('', index, name='homepage'),
    path('profile/<int:user_id>', user_profile_view, name='user_profile'),
    path('user/<str:username>/', UserPostListView.as_view(), name="userposts"),
    path('edit/<int:id>', EditUser)

]
