# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.about, name='about'),
    path(' ', views.home, name='home'),
]