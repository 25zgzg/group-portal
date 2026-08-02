from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Дозволені шляхи для неавторизованих користувачів
        allowed_paths = [
            reverse('accounts:login'),
            reverse('accounts:register'),
            reverse('home'),
            '/api/auth/login/',
            '/api/auth/register/',
        ]

        # Дозволяємо також доступ до адмінки, статичних файлів та всіх маршрутів accounts (allauth тощо)
        if not request.user.is_authenticated:
            if (
                request.path not in allowed_paths 
                and not request.path.startswith('/admin/') 
                and not request.path.startswith('/static/')
                and not request.path.startswith('/accounts/')
            ):
                print(f"DEBUG: Middleware blocking path: {request.path}")
                return redirect('accounts:login')

        response = self.get_response(request)
        return response
