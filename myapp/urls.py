"""
URL configuration for pyjob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import authentication.views
import myapp.views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    
    # timeline URLs

    path('', myapp.views.create_post, name='homepage'),
    path('posts/',myapp.views.post_list,name='posts'),
    path('like-post/',myapp.views.like_post,name="likes"),
    path('delete-post/',myapp.views.delete_post,name='delete_post'),
    path('success/',myapp.views.success,name='success'),
    path('post/<int:post_id>/add_comment/', myapp.views.add_comment, name='add_comment'),
]
