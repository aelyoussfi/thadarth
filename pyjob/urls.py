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
from django.urls import path, include
import authentication.views
import myapp.views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

namespace = 'myapp'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # Authentication URLs
    path('signup', authentication.views.signup_page, name='signup'),
    path('login', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True), 
        name='login',
        ),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_change_done', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
        name='password_change_done'),
    path('password_change', PasswordChangeView.as_view(
        template_name='authentication/password_change.html'),
        name='password_change'),

    # Profile URLs
    path('profile/<str:username>', authentication.views.get_profile, name='profile-page'),
    path('profile/<str:username>/edit', authentication.views.change_profile_photo, name='edit_profile_photo'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)