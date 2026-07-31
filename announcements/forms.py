from django import forms
from .models import AnnouncementComment

class AnnouncementCommentForm(forms.ModelForm):
    class Meta:
        model = AnnouncementComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишіть своє обговорення...'
            }),
        }
        labels = {
            'content': '',
        }
