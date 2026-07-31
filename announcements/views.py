from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Announcement, AnnouncementComment, AnnouncementVote
from .forms import AnnouncementCommentForm

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'

    def get_context_data(f_self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Додаємо підрахунок голосів та кількість коментарів для кожного оголошення
        for ann in context['announcements']:
            ann.likes_count = ann.votes.filter(value=1).count()
            ann.dislikes_count = ann.votes.filter(value=-1).count()
            ann.comments_count = ann.comments.count()
        return context

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

    def get_context_data(f_self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcement = f_self.get_object()
        context['comment_form'] = AnnouncementCommentForm()
        context['comments'] = announcement.comments.select_related('author').all()
        context['likes_count'] = announcement.votes.filter(value=1).count()
        context['dislikes_count'] = announcement.votes.filter(value=-1).count()
        
        if f_self.request.user.is_authenticated:
            user_vote = announcement.votes.filter(user=f_self.request.user).first()
            context['user_vote'] = user_vote.value if user_vote else 0
        else:
            context['user_vote'] = 0
            
        return context

@login_required
def add_announcement_comment(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.author = request.user
            comment.save()
    return redirect('announcements:announcement_detail', pk=announcement.pk)

@login_required
def vote_announcement(request, pk, value):
    announcement = get_object_or_404(Announcement, pk=pk)
    if value not in [1, -1]:
        return redirect('announcements:announcement_detail', pk=announcement.pk)
        
    vote, created = AnnouncementVote.objects.get_or_create(
        announcement=announcement,
        user=request.user,
        defaults={'value': value}
    )
    
    if not created:
        if vote.value == value:
            vote.delete()  # Скасовуємо голос, якщо натиснули те саме
        else:
            vote.value = value
            vote.save()
            
    return redirect('announcements:announcement_detail', pk=announcement.pk)

