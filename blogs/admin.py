from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Tags, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time',)
    list_display_links = ('title',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tags)
