from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.index_title = "Dashboard"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContentInline(admin.StackedInline):
    model = Content
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'reading_time', 'published', 'created_at')
    search_fields = ('title',)
    list_filter = ('views', 'category', 'tags')
    date_hierarchy = 'created_at'
    inlines = (ContentInline,)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at')
    search_fields = ('author', 'text', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
