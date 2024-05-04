from django.contrib import admin
from .models import Content

# Register your models here.


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title', 'url', 'nav_title', 'content_views_short', 'nav_position', 'datetime'
    list_display_links = 'pk', 'title'
