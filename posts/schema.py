import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import (Article, Image, Category, Tag, Comment)
from graphql_jwt.decorators import login_required, staff_member_required
from blog import Connection
from accounts.schema import UserNode
from accounts.models import User


class CommentNode(DjangoObjectType):
    '''Get comments from database'''
    class Meta:
        model = Comment
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'name': ['icontains'],
            'body': ['icontains'],
            'article': ['exact'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt']
        }

    @classmethod
    def get_node(cls, info, id):
        return Comment.objects.get(pk=id)


class AddComment(relay.ClientIDMutation):
    '''Add comments to database'''
    class Input:
        name = graphene.String(required=True)
        body = graphene.String(required=True)
        articleUID = graphene.UUID(required=True)

    comment = graphene.Field(CommentNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        articleUID = kwargs.get('articleUID')
        name = kwargs.get('name')
        body = kwargs.get('body')
        article = Article.objects.get(pk=articleUID)
        comment = Comment(name=name,
                          body=body,
                          article=article)
        comment.save()
        return AddComment(comment=comment)


class TagNode(DjangoObjectType):
    '''Get tags from database'''
    class Meta:
        model = Tag
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'author': ['exact'],
            'name': ['icontains'],
            'slug': ['exact'],
            'articles': ['exact'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt']
        }

    @classmethod
    def get_node(cls, info, id):
        return Tag.objects.get(pk=id)


class CreateTag(relay.ClientIDMutation):
    '''Add tag to database'''
    class Input:
        name = graphene.String(required=True)

    tag = graphene.Field(TagNode)

    @classmethod
    @staff_member_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        name = kwargs.get('name')
        tag = Tag(name=name)
        tag.save()
        return CreateTag(tag=tag)


class ImageNode(DjangoObjectType):
    '''Get images from database'''
    class Meta:
        model = Image
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'name': ['icontains'],
            'article': ['exact'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt']
        }

    @classmethod
    def get_node(csl, info, id):
        return Image.objects.get(pk=id)


class AddImage(relay.ClientIDMutation):
    '''Add image to database'''
    class Input:
        name = graphene.String(required=True)
        url = graphene.String(required=True)
        article = graphene.ID(required=True)

    image = graphene.Field(ImageNode)

    @classmethod
    @staff_member_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        name = kwargs.get('name')
        url = kwargs.get('url')
        article = kwargs.get('article')
        image = Image(name=name,
                      url=url,
                      article=article)
        image.save()
        return AddImage(image=image)


class ArticleNode(DjangoObjectType):
    '''Get articles from database'''
    tags = graphene.List(TagNode)
    images = graphene.List(ImageNode)
    comments = graphene.List(CommentNode)

    class Meta:
        model = Article
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'author': ['exact'],
            'title': ['icontains'],
            'slug': ['exact'],
            'abstract': ['icontains'],
            'body': ['icontains'],
            'category': ['exact'],
            'tags': ['exact'],
            'draft': ['exact'],
            'published': ['gt', 'lt'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt']
        }

    @classmethod
    def get_node(cls, info, id):
        return Article.objects.get(pk=id)

    def resolve_tags(self, info, **kwargs):
        return self.tags.all()

    def resolve_comments(self, info, **kwargs):
        return self.comments.all()

    def resolve_images(self, info, **kwargs):
        return self.images.all()


class CreateArticle(relay.ClientIDMutation):
    '''Add article to database'''
    class Input:
        author = graphene.ID(required=True)
        title = graphene.String(required=True)
        abstract = graphene.String()
        body = graphene.String()
        category = graphene.ID()
        draft = graphene.Boolean(required=True)
        published = graphene.Date()

    article = graphene.Field(ArticleNode)

    @classmethod
    @staff_member_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        author = kwargs.get('author')
        title = kwargs.get('title')
        abstract = kwargs.get('abstract')
        body = kwargs.get('body')
        category = kwargs.get('category')
        draft = kwargs.get('draft')
        published = kwargs.get('published')
        article = Article(author=author,
                          title=title,
                          abstract=abstract,
                          body=body,
                          category=category,
                          draft=draft,
                          published=published)
        article.save()
        return CreateArticle(article=article)


class CategoryNode(DjangoObjectType):
    '''Get categories from database'''
    articles = graphene.List(ArticleNode)

    class Meta:
        model = Category
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'author': ['exact'],
            'name': ['icontains'],
            'slug': ['exact'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt'],
        }

    @classmethod
    def get_node(cls, info, id):
        return Category.objects.get(pk=id)

    def resolve_articles(self, info, **kwargs):
        return self.articles.all()


class CreateCategory(relay.ClientIDMutation):
    '''Add category to database'''
    class Input:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryNode)

    @classmethod
    @staff_member_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        name = kwargs.get('name')
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)


class Query(ObjectType):
    article = relay.Node.Field(ArticleNode)
    articles = DjangoFilterConnectionField(ArticleNode)
    image = relay.Node.Field(ImageNode)
    images = DjangoFilterConnectionField(ImageNode)
    category = relay.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)
    tag = relay.Node.Field(TagNode)
    tags = DjangoFilterConnectionField(TagNode)
    comment = relay.Node.Field(CommentNode)
    comments = DjangoFilterConnectionField(CommentNode)
    node = relay.Node.Field()

    @staff_member_required
    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()


class Mutation(ObjectType):
    create_article = CreateArticle.Field()
    add_image = AddImage.Field()
    create_category = CreateCategory.Field()
    create_tag = CreateTag.Field()
    add_comment = AddComment.Field()
