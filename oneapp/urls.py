from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("aboutme", views.aboutme, ),
    path("login/", views.login_view, name='login')
]