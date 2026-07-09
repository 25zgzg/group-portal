from django.contrib import admin

from .models import Post, Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'created_by__username')
    list_filter = ('created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'created_at')
    search_fields = ('thread__title', 'author__username', 'body')
    list_filter = ('created_at',)
