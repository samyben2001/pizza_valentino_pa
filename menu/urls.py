from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.get_menu, name="menu"),
    path('contact', views.mail_sender, name="contact"),
    path('infos', views.infos, name="infos"),
]
