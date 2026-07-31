from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Акаунт не знайдено або введено неправильний пароль.',
    }


class RegistrationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        user_model = get_user_model()
        if user_model.objects.filter(username__iexact=username).exists():
            raise ValidationError('Цей логін уже зайнятий. Оберіть інший.')
        return username