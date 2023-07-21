from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<a href="">This is a view of app1</a>')

def second(request):
    return HttpResponse('<h1>The class on genaric url mapping is going good...</h1>')
