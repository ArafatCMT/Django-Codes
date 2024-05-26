from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.submit_form, name='submit_form'),
    path('django_form/', views.Django_forms, name= 'django_form'),
    # path('student_form/', views.student_data, name= 'student_form'),
    path('student_form/', views.passwordValidation, name= 'student_form'),
]