from django.contrib import admin
from django.urls import path , include
from project_3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('index/', views.index)
]
