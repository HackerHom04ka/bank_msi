from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class Organization(models.Model):
    title = models.CharField(verbose_name='название', max_length=200)
    description = models.CharField(verbose_name='описание', max_length=400)
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserOrgID')
    count = models.IntegerField(verbose_name='баланс', default=0)
    img = models.ImageField(verbose_name='картинка', blank=True, upload_to='uploads/org', null=True)
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class Comment(models.Model):
    user = models.ForeignKey(verbose_name='ID пользователя', to=settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), related_name='UserOrgComID')
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(verbose_name='дата и время публикции')
    org = models.ForeignKey(verbose_name='ID организации', to='Organization', on_delete=models.CASCADE, related_name='OrgComID')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'