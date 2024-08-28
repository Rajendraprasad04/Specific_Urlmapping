from django.urls import path 
from app1.views import *

urlpatterns = [
    path('today/',today,name='today'),
    path('tomorrow/',tomorrow,name='tomorrow'),
    
]
