from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def articles(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@staff_member_required()
def article_create(request):
    return render(request,'articles/article_create.html')