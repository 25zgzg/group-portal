from django.contrib import admin
from django.db.models import Count
from .models import Thread, Post, PostImage, Vote

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'created_at', 'posts_count']
    list_filter = ['created_at', 'creator']
    search_fields = ['title', 'creator__username', 'creator__email']
    inlines = [PostInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_posts_count=Count('posts'))
        return queryset

    @admin.display(description='Кількість повідомлень', ordering='_posts_count')
    def posts_count(self, obj):
        return obj._posts_count

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'thread_link', 'created_at', 'likes_count', 'dislikes_count']
    list_filter = ['created_at', 'thread__title']
    search_fields = ['content', 'author__username']
    raw_id_fields = ['thread', 'author'] # Зручно для великої кількості даних

    @admin.display(description='Тема')
    def thread_link(self, obj):
        return obj.thread.title

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'is_main']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']
    list_filter = ['value']
