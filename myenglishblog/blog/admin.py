from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create', 'photo', 'video', 'is_published')
    list_display_links = ('id', 'title', 'time_create', 'photo')
    search_fields = ('title', 'content', 'time_create')
    list_filter = ('time_create', 'cat', 'is_published')
    list_editable = ('is_published', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

