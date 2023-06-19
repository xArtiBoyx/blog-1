from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'draft']
    list_filter = ['draft', 'author']
    search_fields = ['title', 'body']
    ordering = ['-draft', '-created_at']
    date_hierarchy = 'changed_at'
