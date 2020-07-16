"""SugarProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

from users.urls import urlpatterns as userurls
from sugar_app.urls import urlpatterns as sugarappurls
from forumapp.urls import urlpatterns as forumappurls
from authentication.urls import urlpatterns as authenticationurls
from sugar_app.views import bad_request
urlpatterns = [
    path('admin/', admin.site.urls),
]

handler404 = bad_request

urlpatterns += userurls + sugarappurls + authenticationurls + forumappurls
