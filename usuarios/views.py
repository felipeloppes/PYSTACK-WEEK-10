from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    print(request.META)
    return HttpResponse('Olá mundo!')