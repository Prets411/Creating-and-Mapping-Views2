from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello!, Welcome to Index Page")

def contact(request):
    msg = "<h3> Email: CSIPT101BARTIANA@gmail.com </br> \
                Telephone: 09211436970 \
            </h3>"
    return HttpResponse(msg)




