from django.urls import path
# from authors.views import register, user_login, user_logout, profile, ChangePassword, edit_profile, UserLoginView
from . import views


urlpatterns = [
    path('register/', views.register, name = 'register'),
    # path('login/', user_login, name = 'login'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    # path('logout/', user_logout, name = 'logout'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('profile/ChangePassword/', views.ChangePassword, name = 'pass_change'),
]