from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nation = models.CharField('национальность', max_length=200, null=True)
    pob = models.CharField('место рождения', max_length=200, null=True)
    por = models.CharField('место проживания', max_length=200, null=True)
    dob = models.CharField('дата рождения', max_length=200, null=True)
    marry = models.CharField('семейное положение', max_length=200, null=True)
    gender = models.CharField('пол', max_length=200, null=True)
    img = models.ImageField('фотокарточка', upload_to='uploads/users', null=True)
    name = models.CharField('ФИО', max_length=200, null=True)
    count = models.IntegerField('мемляр', default=0)