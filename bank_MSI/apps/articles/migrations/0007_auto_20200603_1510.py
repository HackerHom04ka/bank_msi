# Generated by Django 3.0.6 on 2020-06-03 12:10

import articles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_auto_20200524_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/article', verbose_name='титульный рисунок'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(articles.models.get_sentinel_user), related_name='UserArtID', to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArtComID', to='articles.Article', verbose_name='ID статьи'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(articles.models.get_sentinel_user), related_name='UserArtComID', to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя'),
        ),
    ]