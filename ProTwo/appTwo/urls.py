from django.urls import path
from django.conf.urls import include

from appTwo import views

urlpatterns = [
    path('',views.index1,name='index1'),
    ]
