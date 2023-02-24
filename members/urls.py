"""
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
"""


# example/urls.py
from django.urls import path
from members.views import index


urlpatterns = [
    path('', index),
]
"""
# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index),
]
"""