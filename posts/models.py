from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from blog.settings import AUTH_USER_MODEL as User
from django.utils import timezone
from django.urls import reverse
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
                            unique=True,
                            blank=False,
                            null=False)
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

    def get_absolut_url(self):
        pass


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
                            unique=True,
                            blank=False,
                            null=False)
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

    def get_absolut_url(self):
        pass


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
                             unique=True,
                             blank=False,
                             null=False)
    slug = models.SlugField(_('slug'),
                            max_length=150,
                            unique=True)
    body = models.TextField(_('body'),
                            unique=True,
                            blank=True,
                            null=True)
    abstract = models.TextField(_('abstract'),
                                max_length=303,
                                unique=True,
                                blank=True,
                                null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 db_column='category',
                                 blank=True,
                                 null=True)
    tags = models.ManyToManyField(Tag)
    draft = models.BooleanField(_('draft'),
                                default=True)
    published = models.DateField(_('published'),
                                 blank=True,
                                 null=True)
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
        self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_abstract(self):
        return self.abstract

    def get_absolut_url(self):
        pass


class Image(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=50,
                            unique=True,
                            blank=False,
                            null=False)
    slug = models.SlugField(_('slug'),
                            max_length=50,
                            unique=True)
    url = models.ImageField(_('image'),
                            upload_to='images/articles',
                            blank=False,
                            null=False)
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

    def get_absolut_url(self):
        pass


class Comment(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=50,
                            blank=True,
                            null=True)
    body = models.TextField(_('comment'),
                            blank=False,
                            null=False)
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

    def get_absolut_url(self):
        pass
