from django.urls import path
from .views import *
app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_page, name='logout'),
    path('test/', test, name='test'),
    path('register/', register, name='register'),
    path('profile/', view_profile, name='profile')
]