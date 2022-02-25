from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getEPL(request):
    return HttpResponse('EPL')
def getEflChamp(request):
    return HttpResponse('EFL Championship')
def getEfl_L1(request):
    return HttpResponse('EFL League One')
def getEfl_L2(request):
    return HttpResponse('EFL League Two')
def getNL(request):
    return HttpResponse('National League')
