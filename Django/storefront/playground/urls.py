from django.urls import path
from . import views

urlpatterns = [
    path('Home.html', views.say_hello),
    path('BoardGameFinder.html', views.find),
    path('GroupFinder.html', views.group)
]