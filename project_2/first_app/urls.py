from django.urls import path
# from first_app.views import home
from first_app import views

urlpatterns = [
    path("first_app/", views.home),
]