from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('all_users', views.all_users, name='all_users'),
    path('view_user/<user_id>', views.view_user, name="view_user"),
]