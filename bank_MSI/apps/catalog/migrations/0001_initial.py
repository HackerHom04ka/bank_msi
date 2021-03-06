# Generated by Django 3.0.6 on 2020-06-03 12:10

import catalog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.CharField(max_length=400, verbose_name='описание')),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/product', verbose_name='картинка')),
                ('pub_date', models.DateTimeField(verbose_name='дата и время публикции')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=models.SET(catalog.models.get_sentinel_user), related_name='ProOrgID', to='orgs.Organization', verbose_name='ID организации')),
                ('user', models.ForeignKey(on_delete=models.SET(catalog.models.get_sentinel_user), related_name='ProUserID', to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст')),
                ('pub_date', models.DateTimeField(verbose_name='дата и время публикции')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProComID', to='catalog.Product', verbose_name='ID продукта')),
                ('user', models.ForeignKey(on_delete=models.SET(catalog.models.get_sentinel_user), related_name='UserProComID', to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'Комментарий',
            },
        ),
    ]
