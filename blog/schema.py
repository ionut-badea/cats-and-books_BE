import graphene
import graphql_jwt
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from accounts.schema import (Query as Users,
                             Mutation as CreateUser)
from contacts.schema import (Query as Messages,
                             Mutation as AddMessage)
from posts.schema import (Query as Posts,
                          Mutation as CreatePost,
                          MutationComment as AddComment)
from subscription.schema import (Query as Subscribers,
                                 Mutation as AddSubscriber)


class PrivateQuery(
    Messages,
    Subscribers,
    graphene.ObjectType,
):
    pass


class PrivateMutation(
    CreateUser,
    CreatePost,
    graphene.ObjectType,
):
    '''Add objects to database'''
    auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify = graphql_jwt.relay.Verify.Field()
    refresh = graphql_jwt.relay.Refresh.Field()
    revoke = graphql_jwt.relay.Revoke.Field()


class PublicQuery(
    Users,
    Posts,

    graphene.ObjectType,
):
    '''Get objects from database'''
    pass


class PublicMutation(
    AddComment,
    AddMessage,
    AddSubscriber,
    graphene.ObjectType,
):
    pass


public_schema = graphene.Schema(query=PublicQuery, mutation=PublicMutation)
private_schema = graphene.Schema(query=PrivateQuery, mutation=PrivateMutation)
