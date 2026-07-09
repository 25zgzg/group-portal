from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('thread/create/', views.thread_create, name='thread_create'),
    path('thread/<int:pk>/edit/', views.thread_edit, name='thread_edit'),
    path('thread/<int:pk>/delete/', views.thread_delete, name='thread_delete'),
]
