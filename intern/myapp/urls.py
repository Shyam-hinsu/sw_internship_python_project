from django.urls import path

from .views import hello, home

app_name = 'myapp'

urlpatterns = [
    path('hello/', hello),
    path('home/', home,name='home'),



]


