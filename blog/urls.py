from django.urls import path
from .views import all_posts, register, user_login, view_post, add_post, user_dashboard, edit_post, delete_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('all-posts/', all_posts, name='all_posts'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('view-post/<int:post_id>/', view_post, name='view_post'),
    path('add-post/', add_post, name='add_post'), 
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('edit-post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete-post/<int:post_id>/', delete_post, name='delete_post'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
