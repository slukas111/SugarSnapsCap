from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SugarProject import settings
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('postcreate/', PostCreateView.as_view(), name='postcreate'),
    path('post/<str:slug>/', PostDetailView.as_view(), name="postdetail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="postupdate"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="postdelete"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

