from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Post, Comment, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'status', 'views_count', 'created_at')
    list_filter = ('status', 'category', 'author', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    # Возможность редактировать статус прямо в списке
    list_editable = ('status',)
    # Поля только для чтения (просмотры не редактируются вручную)
    readonly_fields = ('views_count',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('text',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birth_date', 'avatar_preview')
    search_fields = ('user__username', 'bio')
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        """Отображает круглую миниатюру аватарки в списке профилей."""
        if obj.avatar:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; '
                'border-radius: 50%; object-fit: cover;" />',
                obj.avatar.url
            )
        return "Нет аватарки"

    avatar_preview.short_description = 'Аватар'