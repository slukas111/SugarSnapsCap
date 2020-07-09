from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SugarProject import settings
from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('postcreate/', PostCreateView.as_view(template_name='boxform.html')),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='boxitemdetail.html'), name="postdetail"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

