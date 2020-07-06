from django.db import models
from django.db.models.functions import Extract
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from blog.settings import AUTH_USER_MODEL as User
from django.utils import timezone
from django.urls import reverse
import datetime
import uuid


class Category(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    author = models.ForeignKey(User,
                               on_delete=models.DO_NOTHING,
                               db_column='author')
    name = models.CharField(_('category'),
                            max_length=50,
                            unique=True)
    slug = models.SlugField(_('slug'),
                            unique=True,
                            max_length=50)
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        default_related_name = 'categories'
        ordering = ['name']
        get_latest_by = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    author = models.ForeignKey(User,
                               on_delete=models.DO_NOTHING,
                               db_column='author')
    name = models.CharField(_('tag'),
                            max_length=25,
                            unique=True)
    slug = models.SlugField(_('slug'),
                            max_length=25,
                            unique=True)
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        default_related_name = 'tags'
        ordering = ['name']
        get_latest_by = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    author = models.ForeignKey(User,
                               on_delete=models.DO_NOTHING,
                               db_column='author')
    title = models.CharField(_('title'),
                             max_length=150,
                             unique=True)
    slug = models.SlugField(_('slug'),
                            max_length=150,
                            unique=True)
    body = models.TextField(_('body'),
                            blank=True)
    abstract = models.TextField(_('abstract'),
                                max_length=303,
                                blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 db_column='category',
                                 blank=True)
    tags = models.ManyToManyField(Tag,
                                  blank=True)
    draft = models.BooleanField(_('draft'),
                                default=True)
    published = models.DateTimeField(_('published'),
                                     blank=True,
                                     null=True)
    year = models.PositiveIntegerField(_('year'),
                                       blank=True,
                                       null=True,
                                       editable=False)
    month = models.PositiveIntegerField(_('month'),
                                        blank=True,
                                        null=True,
                                        editable=False)
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        default_related_name = 'articles'
        ordering = ['-published', 'title']
        get_latest_by = ['-created']

    def save(self, *args, **kwargs):
        if(not self.abstract and len(self.body) > 300):
            self.abstract = f'{self.body[0:300]}...'
        elif(not self.abstract and len(self.body) < 300):
            self.abstract = f'{self.body}'
        # if self.published:
        #     print("published DATE", self.published)
        #     self.year = Extract(self.published, 'year')
        #     self.month = Extract(self.published, 'month')
        self.slug = slugify(self.title)

        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=50,
                            unique=True)
    slug = models.SlugField(_('slug'),
                            max_length=50,
                            unique=True)
    url = models.ImageField(_('image'),
                            upload_to='images/articles')
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                db_column='article')
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        default_related_name = 'images'
        ordering = ['article']
        get_latest_by = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.article}, {self.name}'

    def get_url(self):
        return self.url


class Comment(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=50,
                            blank=True)
    body = models.TextField(_('comment'))
    reviewed = models.BooleanField(_('reviewed'),
                                   default=False)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                db_column='article')
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        default_related_name = 'comments'
        ordering = ['name']
        get_latest_by = ['-created']

    def __str__(self):
        return f'{self.name}, {self.body}'
