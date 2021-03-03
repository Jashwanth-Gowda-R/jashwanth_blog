from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from . import forms


# Create your views here.
def articles(request):
    articles = Articles.objects.all().order_by('-date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@staff_member_required()
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticles(request.POST, request.FILES)
        if form.is_valid():
            # saving to db with author attached
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticles()
    return render(request, 'articles/article_create.html', {'form': form})
