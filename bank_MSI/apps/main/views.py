from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
from orgs.models import Organization
from country.models import Country
from catalog.models import Product

# Create your views here.
def index(request):
    catalog = Product.objects.order_by('-pub_date')[:3]
    country = Country.objects.order_by('-pub_date')[:3]
    articles = Article.objects.order_by('-pub_date')[:3]
    orgs = Organization.objects.order_by('pub_date')[:3]
    return render(request, 'main/main.html', {'article': articles, 'catalog': catalog, 'country': country, 'org': orgs})