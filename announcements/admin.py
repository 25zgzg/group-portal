from django.contrib import admin
from .models import Announcement, AnnouncementComment, AnnouncementVote

class CommentInline(admin.TabularInline):
    model = AnnouncementComment
    extra = 0
    readonly_fields = ['created_at']

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_display_links = ['id']
    list_editable = ['title']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content', 'author__username']
    inlines = [CommentInline]

@admin.register(AnnouncementComment)
class AnnouncementCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'announcement', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'author__username']

@admin.register(AnnouncementVote)
class AnnouncementVoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'announcement', 'value']
    list_filter = ['value']
