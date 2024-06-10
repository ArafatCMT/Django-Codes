from django.urls import path
from categoris.views import add_category

urlpatterns = [
    path('add/', add_category, name = 'add_category'),
]