import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Article, Category, Comment

# Create your views here.

def articles(request, pk):
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        article_list = Article.objects.all()
        category = u''
    return render(request, 'blog/articles.html', {"article_list": article_list,
                                                  "category": category})



def home_view(*args, **kwargs):
    return HttpResponse('<h1> wo shi hao ren </h1>')
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1> Hello Word </h1>")  # string of HTML code
    # return render(request, "home.html", {})  # empty dictionary

def contact_view(*args, **kwargs):
    return HttpResponse("<h1> Contact Pages </h1>")

def about_view(*args, **kwargs):
    return HttpResponse("<h1> About Page </h1>")

def social_view(*args, **kwargs):
    return HttpResponse("<h1> Social View </h1>")

