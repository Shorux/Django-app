from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужние'),
            ('single', 'Не замужние')
        ]

    def queryset(self, request, queryset):
        return queryset


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'cat')
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    list_editable = ('is_published', )
    list_per_page = 5
    ordering = ('-time_create', 'title')
    actions = ('set_published', 'set_draft')
    search_fields = ('title__startswith', 'cat__name')
    list_filter = ('cat__name', 'is_published')

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
