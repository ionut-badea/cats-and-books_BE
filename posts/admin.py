from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (Article,
                     Image,
                     Category,
                     Tag,
                     Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('author', 'name',)}),
    )
    list_display = ('name', 'created')
    list_filter = ('author', 'name', 'created')
    search_fields = ('author__username', 'author__first_name',
                     'author__last_name', 'name__icontains')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('author', 'name')}),
    )
    list_display = ('name', 'created')
    list_filter = ('author', 'name', 'created')
    search_fields = ('author__username', 'author__first_name',
                     'author__last_name', 'name__icontains')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('author',)}),
        (_('Article'), {'fields': ('title',
                                   'body',
                                   'abstract',
                                   'category',
                                   'tags')}),
        (_('Publish'), {'fields': ('draft', 'published')})
    )

    list_display = ('title', 'author', 'category',
                    'draft', 'published')
    list_filter = ('author', 'category', 'tags', 'draft', 'published')
    search_fields = ('author__username', 'author__first_name',
                     'author__last_name', 'title__icontains',
                     'body__icontains', 'abstract__icontains',
                     'category__icontains', 'tags__icontains')
    filter_horizontal = ('tags',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'image', 'article')}),
    )

    list_display = ('name', 'article', 'created')
    list_filter = ('name', 'article', 'created')
    search_fields = ('name__icontains', 'article__title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'body')}),
        (_('Article'), {'fields': ('article',)})
    )
    list_display = ('name', 'article', 'created')
    list_filter = ('name', 'article', 'created')
    search_fields = ('name__icontains', 'body__icontains', 'article__title')
