from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('',views.articles,name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail,name="details"),
]
# This has been significantly changed in Django 3, this could be done like this:
# path('<slug:slug>/', views.article_detail),
# where the first slug "<slug" is the type of the passed parameter which is a slug in our case, and the second slug ":slug>" is the name of the parameter which could be any name; "abc", "the_slug", etc.
# If you still insist to use regex then there is one thing to change; the method name instead of "url" use "re_path":
# re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),