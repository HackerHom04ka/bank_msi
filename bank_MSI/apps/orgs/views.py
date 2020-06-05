from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Organization, Comment

# Create your views here.
def index(request):
    org = Organization.objects.order_by('-pub_date')
    return render(request, 'articles/index.html', {'org': org})


def detail(request, id):
    try:
        o = Organization.objects.get( id = id )
    except:
        raise Http404('Не найдено (Либо удалено, либо не существовало)')

    return render(request, 'articles/detail.html', {'o': o})