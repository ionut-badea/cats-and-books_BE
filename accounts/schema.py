import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required, superuser_required
from .models import User
from blog import Connection
from django.contrib.auth.models import Group, Permission, ContentType


class ContentTypeNode(DjangoObjectType):
    '''Get content types from database'''
    class Meta:
        model = ContentType
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            'app_label': ['icontains'],
            'model': ['icontains'],
            'permission': ['exact']
        }

    @classmethod
    @superuser_required
    def get_node(cls, info, id):
        return ContentType.objects.get(pk=id)


class CreateContentType(relay.ClientIDMutation):
    '''Add content type to database'''
    class Input:
        app_label = graphene.String(required=True)
        model = graphene.String(required=True)

    content_type = graphene.Field(ContentTypeNode)

    @classmethod
    @superuser_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        app_labe = kwargs.get('app_label')
        model = kwargs.get('models')
        content_type = ContentType(app_labe=app_labe,
                                   model=model)
        content_type.save()
        return CreateContentType(content_type=content_type)


class PermissionNode(DjangoObjectType):
    '''Get permissions from database'''
    class Meta:
        model = Permission
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            'name': ['icontains'],
            'content_type': ['exact'],
            'codename': ['icontains'],
            'user': ['exact'],
            'group': ['exact']
        }

    @classmethod
    @superuser_required
    def get_node(cls, info, id):
        return Permission.objects.get(pk=id)


class CreatePermission(relay.ClientIDMutation):
    '''Add permission to database'''
    class Input:
        name = graphene.String(required=True)
        content_type = graphene.ID(required=True)
        codename = graphene.String(required=True)

    permission = graphene.Field(PermissionNode)

    @classmethod
    @superuser_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        name = kwargs.get('name')
        content_type = kwargs.get('content_type')
        codename = kwargs.get('codename')
        permission = Permission(name=name,
                                content_type=content_type,
                                codename=codename)
        permission.save()
        return CreatePermission(permission=permission)


class GroupNode(DjangoObjectType):
    '''Get groups from database'''
    permissions = graphene.List(PermissionNode)

    class Meta:
        model = Group
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            'name': ['icontains'],
            'permissions': ['exact'],
            'user': ['exact']
        }

    @classmethod
    @superuser_required
    def get_node(cls, info, id):
        return Group.objects.get(pk=id)

    @superuser_required
    def resolve_permissions(self, info, **kwargs):
        return self.permissions.all()


class CreateGroup(relay.ClientIDMutation):
    '''Add group to database'''
    class Input:
        name = graphene.String(required=True)
        permissions = graphene.ID()

    group = graphene.Field(GroupNode)

    @classmethod
    @superuser_required
    def mutate_and_get_payload(cls, root, info, **kwargs):
        name = kwargs.get('name')
        permissions = kwargs.get('permissions')
        group = Group(name=name,
                      permissions=permissions)
        group.save()
        return CreateGroup(group=group)


class UserNode(DjangoObjectType):
    '''Get users from database'''
    groups = graphene.List(GroupNode)
    permissions = graphene.List(PermissionNode)

    class Meta:
        model = User
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'username': ['exact', 'icontains'],
            'email': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'is_active': ['exact'],
            'is_staff': ['exact'],
            'is_superuser': ['exact'],
            'groups': ['exact'],
            'user_permissions': ['exact'],
            'last_login': ['exact', 'gt', 'lt'],
            'date_joined': ['exact', 'gt', 'lt']
        }

    @classmethod
    @login_required
    def get_node(cls, info, id):
        user = info.context.user
        user_db = User.objects.get(pk=id)
        if user == user_db or user.is_superuser:
            return user_db

    @login_required
    def resolve_groups(self, info, **kwargs):
        return self.groups.all()

    @login_required
    def resolve_permissions(self, info, **kwargs):
        return self.user_permissions.all()


class CreateUser(relay.ClientIDMutation):
    '''Add user to database'''
    class Input:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        bio = graphene.String()

    user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        bio = kwargs.get('bio')
        user = get_user_model()(username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                bio=bio)
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
    group = relay.Node.Field(GroupNode)
    groups = DjangoFilterConnectionField(GroupNode)
    content_type = relay.Node.Field(ContentTypeNode)
    content_types = DjangoFilterConnectionField(ContentTypeNode)
    permission = relay.Node.Field(PermissionNode)
    permissions = DjangoFilterConnectionField(PermissionNode)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    @superuser_required
    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()

    @superuser_required
    def resolve_permissions(self, info, **kwargs):
        return Permission.objects.all()

    @superuser_required
    def resolve_content_types(self, info, **kwargs):
        return ContentType.objects.all()


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_group = CreateGroup.Field()
    create_content_type = CreateContentType.Field()
    create_permission = CreatePermission.Field()
