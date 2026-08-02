from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
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
