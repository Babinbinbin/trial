from django.contrib import admin
from .models import Article, Content
# Register your models here.
class ContentInline(admin.TabularInline):
    model= Content
class ArticleAdmin(admin.ModelAdmin):
    inlines= [ContentInline]

admin.site.register(Article)
admin.site.register(Content)
 
