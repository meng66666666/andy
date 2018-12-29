from django.urls import path

from beauty.views import *

app_name = 'beauty'
urlpatterns = [
    path('goreg/', go_register),
    path('login/',login,name='login')
]