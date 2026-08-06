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

    actions = ['make_moderator', 'make_admin', 'activate_users', 'deactivate_users']

    @admin.action(description='Надати роль Модератора')
    def make_moderator(self, request, queryset):
        if not request.user.is_superuser:
            self.message_user(request, "Лише суперкористувач може змінювати ролі.", level='error')
            return
        queryset.update(role=User.ROLE_MODERATOR)

    @admin.action(description='Надати роль Адміністратора')
    def make_admin(self, request, queryset):
        if not request.user.is_superuser:
            self.message_user(request, "Лише суперкористувач може змінювати ролі.", level='error')
            return
        queryset.update(role=User.ROLE_ADMIN)

    @admin.action(description='Активувати обраних користувачів')
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Деактивувати обраних користувачів (Soft Delete)')
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return list(readonly_fields) + ['is_superuser', 'is_staff', 'role', 'user_permissions', 'groups']
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'followed', 'created_at']
    list_filter = ['created_at']
    search_fields = ['follower__username', 'followed__username']
