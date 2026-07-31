from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    add_announcement_comment,
    vote_announcement,
)

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('<int:pk>/comment/', add_announcement_comment, name='add_comment'),
    path('<int:pk>/vote/<int:value>/', vote_announcement, name='vote'),
]

