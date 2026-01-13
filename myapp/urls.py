from django.urls import path
from .views import *
app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),
    path('products/<int:id>/', products, name='products'),
    path('prodetails/<int:id>/', pdetails, name='details')
]