# Generated by Django 3.0.6 on 2020-05-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.CharField(max_length=200, null=True, verbose_name='дата рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=200, null=True, verbose_name='пол'),
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(null=True, upload_to='uploads/users', verbose_name='фотокарточка'),
        ),
        migrations.AddField(
            model_name='user',
            name='marry',
            field=models.CharField(max_length=200, null=True, verbose_name='семейное положение'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='user',
            name='nation',
            field=models.CharField(max_length=200, null=True, verbose_name='национальность'),
        ),
        migrations.AddField(
            model_name='user',
            name='pob',
            field=models.CharField(max_length=200, null=True, verbose_name='место рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='por',
            field=models.CharField(max_length=200, null=True, verbose_name='место проживания'),
        ),
    ]
