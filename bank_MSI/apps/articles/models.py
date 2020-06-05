from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name='название', max_length=200)
    img = models.ImageField(verbose_name='титульный рисунок', blank=True, upload_to='uploads/article', null=True)
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserArtID')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comment(models.Model):
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserArtComID')
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')
    article = models.ForeignKey(verbose_name='ID статьи', to='Article', on_delete=models.CASCADE, related_name='ArtComID')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'