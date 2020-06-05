from django.urls import path, include
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('id<int:id>/', views.detail, name='detail'),
    path('id<int:id>/add_comment', views.comment, name='comment'),
]