from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from forum.models import Thread
from announcements.models import Announcement

def is_moderator_or_higher(user):
    return user.is_authenticated and (user.is_moderator or user.is_administrator or user.is_superuser)

@login_required
@user_passes_test(is_moderator_or_higher, login_url='/accounts/login/')
def moderation_dashboard(request):
    threads = Thread.objects.all().order_by('-created_at')[:15]
    announcements = Announcement.objects.all().order_by('-created_at')[:15]
    context = {
        'threads': threads,
        'announcements': announcements,
    }
    return render(request, 'moderation/dashboard.html', context)

@login_required
@user_passes_test(is_moderator_or_higher, login_url='/accounts/login/')
def delete_thread_mod(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.delete()
    return redirect('moderation:dashboard')

@login_required
@user_passes_test(is_moderator_or_higher, login_url='/accounts/login/')
def delete_announcement_mod(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.delete()
    return redirect('moderation:dashboard')
