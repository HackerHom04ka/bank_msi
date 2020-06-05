from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Country, Comment

# Create your views here.
def index(request):
    country = Country.objects.order_by('-pub_date')
    return render(request, 'country/index.html', {'country': country})


def detail(request, id):
    try:
        c = Country.objects.get( id = id )
    except:
        raise Http404('Не найдено (Либо удалено, либо не существовало)')

    return render(request, 'country/detail.html', {'c': c})