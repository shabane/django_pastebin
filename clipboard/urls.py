from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logout', views.logout),
    path('support', views.support),
    path('action/delete', views.delete)
]