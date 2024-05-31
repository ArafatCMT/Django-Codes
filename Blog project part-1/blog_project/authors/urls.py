from django.urls import path
from authors.views import add_author
urlpatterns = [
    path('add/', add_author, name = 'add_author'),
]