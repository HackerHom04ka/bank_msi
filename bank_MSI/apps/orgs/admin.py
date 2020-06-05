from django.contrib import admin
from .models import Organization, Comment

# Register your models here.
admin.site.register(Organization)
admin.site.register(Comment)