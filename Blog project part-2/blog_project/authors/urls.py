from django.urls import path
from authors.views import register, user_login, user_logout, profile, ChangePassword, edit_profile
urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('profile/ChangePassword/', ChangePassword, name = 'pass_change'),
]