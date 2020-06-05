from django.urls import path, include
from . import views

app_name = 'country'
urlpatterns = [
    path('', views.index, name='index'),
    path('id<int:id>/', views.detail, name='detail'),
]