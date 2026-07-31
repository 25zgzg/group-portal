from django import forms
from .models import Thread, Post

# Custom widget to support multiple file uploads
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
            return result
        return single_file_clean(data, initial)

class ThreadForm(forms.ModelForm):
    content = forms.CharField(
        label="Зміст повідомлення",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Опишіть суть теми...'}),
        required=True
    )
    images = MultipleFileField(
        label="Зображення (можна декілька)",
        required=False
    )

    class Meta:
        model = Thread
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва теми'}),
        }

class PostForm(forms.ModelForm):
    images = MultipleFileField(
        label="Зображення (можна декілька)",
        required=False
    )
    
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
