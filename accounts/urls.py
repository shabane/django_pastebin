from django.urls import path
from django.urls.resolvers import URLPattern
from .views import singup

urlpatterns = [
    path('', singup)
]