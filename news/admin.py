from django.contrib import admin

# Register your models here.

from .models import TextNews, NewsHeadline

admin.site.register(NewsHeadline)
admin.site.register(TextNews)
