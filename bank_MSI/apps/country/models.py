from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class Country(models.Model):
    title = models.CharField(verbose_name='название', max_length=200)
    description = models.CharField(verbose_name='описание', max_length=400)
#    vk_group = models.IntegerField(verbose_name='ID группы в ВК')
    img = models.ImageField(verbose_name='картинка', blank=True, upload_to='uploads/country', null=True)
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserConID')
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Comment(models.Model):
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserConComID')
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')
    country = models.ForeignKey(verbose_name='ID страны', to='Country', on_delete=models.CASCADE, related_name='ConComID')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'