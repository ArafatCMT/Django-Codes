from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'homepage'),
    path('author/', include('authors.urls')),
    path('category/', include('categoris.urls')),
    path('post/', include('posts.urls')),
    path('profile/', include('profiles.urls')),
]
