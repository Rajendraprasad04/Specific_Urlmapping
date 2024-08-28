from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def today(request):
    return HttpResponse('<center><h1>today is monday</h1></center>')
def tomorrow(request):
    return render(request,'tomorrow.html')
