from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
# Create your views here.
def articles(request):
    articles=Articles.objects.all().order_by('date')
    return render(request, 'articles/articles.html',{'articles':articles})

def article_detail(request,slug):
    return HttpResponse(slug)
