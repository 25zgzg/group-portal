from django.contrib import admin
from .models import Post, Thread

<<<<<<< HEAD
from .models import Post, Thread

=======
>>>>>>> 9252d2e2541eddd7772fa14580e417d85b75034c

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at')
    search_fields = ('title', 'creator__username')
    list_filter = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'created_at')
    search_fields = ('thread__title', 'author__username', 'body')
<<<<<<< HEAD
    list_filter = ('created_at',)
=======
    list_filter = ('created_at',)
>>>>>>> 9252d2e2541eddd7772fa14580e417d85b75034c
