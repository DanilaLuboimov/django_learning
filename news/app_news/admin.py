from django.contrib import admin
from .models import News, Comment


class NewsInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'update_at', 'flag_action')
    list_filter = ['flag_action']
    inlines = [NewsInLine]

    actions = ['set_active', 'set_inactive']

    def set_active(self, request, queryset):
        queryset.update(flag_action=1)

    def set_inactive(self, request, queryset):
        queryset.update(flag_action=0)

    set_active.short_description = 'Сделать новость активной'
    set_inactive.short_description = 'Сделать новость неактивной'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'short_comment', 'news')
    list_filter = ['username']
    actions = ['delete_comment']

    @staticmethod
    def short_comment(username):
        comment = Comment.objects.get(username=username)

        if len(comment.text) > 15:
            return comment.text[:15:] + '...'
        else:
            return comment.text

    def delete_comment(self, request, queryset):
        queryset.update(text='Комментарий удален Администратором')

    delete_comment.short_description = 'Удалить текст комментария'
