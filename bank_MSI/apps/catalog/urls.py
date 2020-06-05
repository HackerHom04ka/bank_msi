from django.urls import path, include
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('id<int:id>/', views.detail, name='detail'),
]