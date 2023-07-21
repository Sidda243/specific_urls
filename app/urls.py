
from django.urls import path
from app.views import *
app_name='my_first'
urlpatterns = [
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]