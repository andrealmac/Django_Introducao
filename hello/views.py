from django.http import response
from django.shortcuts import render, HttpResponse

def hello(request):
    response = 'Andre'
    return HttpResponse(response)
