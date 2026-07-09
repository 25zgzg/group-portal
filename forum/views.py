import re

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django import forms

from .models import Post, Thread


def normalize_text(value: str) -> str:
    return re.sub(r'\s+', ' ', value or '').strip()


def staff_required(view_func):
    return user_passes_test(lambda user: user.is_staff)(view_func)


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введіть назву гілки', 'class': 'form-control'}),
        }

    def clean_title(self):
        title = normalize_text(self.cleaned_data.get('title', ''))
        if not title:
            raise forms.ValidationError('Назва гілки не може бути порожньою.')
        if len(title) < 3:
            raise forms.ValidationError('Назва гілки має містити щонайменше 3 символи.')
        return title


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Напишіть повідомлення у гілці',
                'class': 'form-control',
            }),
        }

    def clean_body(self):
        body = normalize_text(self.cleaned_data.get('body', ''))
        if not body:
            raise forms.ValidationError('Повідомлення не може бути порожнім.')
        if len(body) < 5:
            raise forms.ValidationError('Повідомлення має містити щонайменше 5 символів.')
        return body


@login_required
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'thread_list.html', {'threads': threads})


@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = thread.posts.select_related('author')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                thread=thread,
                author=request.user,
                body=form.cleaned_data['body'],
            )
            return redirect(reverse('forum:thread_detail', args=[thread.pk]))
    else:
        form = PostForm()

    return render(request, 'thread_detail.html', {
        'thread': thread,
        'posts': posts,
        'form': form,
    })


@login_required
@staff_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user
            thread.save()
            return redirect(reverse('forum:thread_detail', args=[thread.pk]))
    else:
        form = ThreadForm()

    return render(request, 'thread_form.html', {
        'form': form,
        'title': 'Створити нову гілку',
    })


@login_required
@staff_required
def thread_edit(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect(reverse('forum:thread_detail', args=[thread.pk]))
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'thread_form.html', {
        'form': form,
        'title': 'Редагувати гілку',
    })


@login_required
@staff_required
def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        thread.delete()
        return redirect(reverse('forum:thread_list'))
    return render(request, 'thread_form.html', {
        'form': None,
        'title': 'Видалити гілку',
        'thread': thread,
        'delete_confirmation': True,
    })
