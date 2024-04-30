from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import all_posts

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('all-posts/', all_posts, name='all_posts'),
    path('', include('blog.urls')),
]
