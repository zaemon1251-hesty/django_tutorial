from django.urls import path
from . import views

app_name = 'shift'

urlpatterns = [
    path('', views.index, name='index'),
]
