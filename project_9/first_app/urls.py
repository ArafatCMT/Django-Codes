from django.urls import path
from first_app.views import home, get_cookie, delete_cookie, set_session, get_session, delete_session

urlpatterns = [
    path('', set_session),
    path('get/', get_session),
    path('del/', delete_session)
]
