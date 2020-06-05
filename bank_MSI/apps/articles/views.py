from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment

# Create your views here.
def index(request):
    article = Article.objects.order_by('-pub_date')
    return render(request, 'articles/index.html', {'article': article})


def detail(request, id):
    try:
        a = Article.objects.get( id = id )
    except:
        raise Http404('Не найдено (Либо удалено, либо не существовало)')

    return render(request, 'articles/detail.html', {'a': a})

def comment(request, id):
    try:
        a = Article.objects.get( id = id )
    except:
        raise Http404('Не найдено (Либо удалено, либо не существовало)')

    return render(request, 'articles/detail.html', {'a': a})