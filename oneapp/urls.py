from urllib.parse import urlparse
from django.urls import path
from . import views


#app_name = 'oneapp' #! this needs to be uncommented if we will use namespaces for routing
urlpatterns = [
    path("", views.index, name="index"),
    path("aboutme", views.aboutme, name='aboutme' ),
    path("bootstrap", views.bootstrap, name='bootstrap' ),
    path("item", views.item, name='item' )  #! we add this new view
]

