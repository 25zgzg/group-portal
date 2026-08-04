from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        
        # Генерація унікального username
        if not user.username and user.email:
            base_username = user.email.split('@')[0]
            username = base_username
            User = get_user_model()
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}_{counter}"
                counter += 1
            user.username = username
        
        # Встановлення неможливого пароля для соц-користувачів
        if not user.has_usable_password():
            user.set_unusable_password()

        # Синхронізація аватарки
        if sociallogin.account.provider == 'google':
            picture = sociallogin.account.extra_data.get('picture')
            if picture:
                user.avatar = picture
                
        return user

    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            if sociallogin.account.provider == 'google':
                picture = sociallogin.account.extra_data.get('picture')
                if picture and not sociallogin.user.avatar:
                    sociallogin.user.avatar = picture
                    sociallogin.user.save()
        return super().pre_social_login(request, sociallogin)
