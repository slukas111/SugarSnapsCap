from django.urls import path

from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('postcreate/', PostCreateView.as_view(template_name='boxform.html')),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='boxitemdetail.html'), name="postdetail"),
]

