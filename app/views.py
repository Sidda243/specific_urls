from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return  HttpResponse('<h1>Genaric Url mapping class is going on</h1>')

def second(request):
    return  HttpResponse('<marquee><h1>Hello how was todays class?</h1></marquee>')