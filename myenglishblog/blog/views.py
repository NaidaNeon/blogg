from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *

menu = [{'title':'About us', 'url_name': 'about'},
        {'title':'Add a post', 'url_name': 'add_post'},
        {'title':'Contact us', 'url_name': 'contact'},
        {'title':'Login', 'url_name': 'login'}
]

def index(request):
    posts = Blog.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title':'Main page',
        'cat_selected': 0,
    }

    return render(request, 'blogtemplates/index.html', context=context)

def about(request):
    return render(request, 'blogtemplates/about.html', {'title':'About us'})

def addpost(request):
    return HttpResponse('Add a new post')

def contact(request):
    return HttpResponse('Here you can find our contacts')

def login(request):
    return HttpResponse('Page to login or signup')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found. Try again</h1>')

def show_post(request, post_id):
    return HttpResponse(f'An article with id = {post_id}')


def show_category(request, cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Categories',
        'cat_selected': cat_id,
    }

    return render(request, 'blogtemplates/index.html', context=context)

