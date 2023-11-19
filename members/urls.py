# members/urls.py

from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/control/<int:id>/', views.control, name='control'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('members/object/<int:id>/', views.object, name='object'),
    path('members/function/<int:id>/', views.fun, name='fun'),
    path('add_topic/', views.add_topic, name='add_topic'),
]
