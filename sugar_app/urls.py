from django.urls import path

from .views import PostCreateView

urlpatterns = [
    path('postcreate/', PostCreateView.as_view(template_name='boxform.html'))
]
