from django.contrib import admin

from booking_manager.models import Comment


@admin.action(description='Опубликовать выбранные комментарии')
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description='Убрать выбранные комментарии')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'client',
        'barber',
        'is_published',
        'rating'
    ]

    list_filter = [
        'rating',
        'is_published'
    ]
    actions = [
        make_published,
        make_unpublished
    ]