from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Follow

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering = ['email']

    # Додаємо наші поля в інтерфейс редагування
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Додаткова інформація', {'fields': ('role', 'avatar')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Додаткова інформація', {'fields': ('role', 'avatar')}),
    )

    actions = ['make_moderator', 'make_admin']

    @admin.action(description='Надати роль Модератора')
    def make_moderator(self, request, queryset):
        queryset.update(role=User.ROLE_MODERATOR)

    @admin.action(description='Надати роль Адміністратора')
    def make_admin(self, request, queryset):
        queryset.update(role=User.ROLE_ADMIN)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'followed', 'created_at']
    list_filter = ['created_at']
    search_fields = ['follower__username', 'followed__username']
