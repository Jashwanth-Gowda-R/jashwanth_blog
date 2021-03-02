from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')
def about(request):
    # return HttpResponse('about vrook')
    return render(request,'about.html')

def contact(request):
    # return HttpResponse('about vrook')
    return render(request,'contact.html')

def tos(request):
    # return HttpResponse('about vrook')
    return render(request,'tos.html')

def privacy(request):
    # return HttpResponse('about vrook')
    return render(request,'privacy.html')

def team(request):
    # return HttpResponse('about vrook')
    return render(request,'team.html')