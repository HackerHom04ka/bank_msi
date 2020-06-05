from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Product, Comment

# Create your views here.
def index(request):
    product = Product.objects.order_by('-pub_date')
    return render(request, 'catalog/index.html', {'catalog': product})


def detail(request, id):
    try:
        p = Product.objects.get( id = id )
    except:
        raise Http404('Не найдено (Либо удалено, либо не существовало)')

    return render(request, 'catalog/detail.html', {'p': p})