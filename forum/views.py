from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from accounts.models import Follow
from .models import Thread, Post, PostImage, Vote
from .forms import ThreadForm, PostForm

class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    context_object_name = 'threads'

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/thread_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        thread = form.save()
        
        # Створюємо перший пост у темі
        content = form.cleaned_data.get('content')
        post = Post.objects.create(
            thread=thread,
            author=self.request.user,
            content=content
        )
        
        # Обробка зображень
        images = self.request.FILES.getlist('images')
        for i, img in enumerate(images):
            PostImage.objects.create(post=post, image=img, is_main=(i == 0))
            
        self.object = thread
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('forum:thread_detail', kwargs={'pk': self.object.pk})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/post_form.html'

    def form_valid(self, form):
        thread = get_object_or_404(Thread, pk=self.kwargs['thread_pk'])
        form.instance.thread = thread
        form.instance.author = self.request.user
        response = super().form_valid(form)
        
        # Обробка зображень
        images = self.request.FILES.getlist('images')
        for i, img in enumerate(images):
            PostImage.objects.create(post=self.object, image=img, is_main=(i == 0))
            
        return response

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.kwargs['thread_pk']})

@login_required
def vote_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    value = int(request.POST.get('value', 0))
    if value in [1, -1]:
        vote, created = Vote.objects.get_or_create(post=post, user=request.user, defaults={'value': value})
        if not created:
            if vote.value == value:
                vote.delete()
            else:
                vote.value = value
                vote.save()
        
        # Перераховуємо лічильники
        post.likes_count = post.votes.filter(value=1).count()
        post.dislikes_count = post.votes.filter(value=-1).count()
        post.save()
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'likes_count': post.likes_count,
                'dislikes_count': post.dislikes_count
            })
        
    return redirect('forum:thread_detail', pk=post.thread.pk)

@login_required
def toggle_follow(request, author_pk):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    author = get_object_or_404(User, pk=author_pk)
    if author != request.user:
        follow, created = Follow.objects.get_or_create(follower=request.user, followed=author)
        if not created:
            follow.delete()
    return redirect(request.META.get('HTTP_REFERER', 'thread_list'))

