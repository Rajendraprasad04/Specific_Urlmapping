from django.urls import path
from app2.views import *
urlpatterns = [
    path('table/',table,name='table'),
    
]
