from django.urls import path
from .views import (
    ThreadListView, ThreadDetailView, ThreadCreateView, 
    PostCreateView, vote_post, toggle_follow
)

app_name = 'forum'

urlpatterns = [
    path('', ThreadListView.as_view(), name='thread_list'),
    path('create/', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('<int:thread_pk>/post/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_pk>/vote/', vote_post, name='vote_post'),
    path('follow/<int:author_pk>/', toggle_follow, name='toggle_follow'),
]

