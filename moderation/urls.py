from django.urls import path
from .views import moderation_dashboard, delete_thread_mod, delete_announcement_mod

app_name = 'moderation'

urlpatterns = [
    path('', moderation_dashboard, name='dashboard'),
    path('thread/<int:pk>/delete/', delete_thread_mod, name='delete_thread'),
    path('announcement/<int:pk>/delete/', delete_announcement_mod, name='delete_announcement'),
]
