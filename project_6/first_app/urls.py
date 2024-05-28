from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('delete_data/<int:roll>', views.delete_student, name = 'delete_student'),
]