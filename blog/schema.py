import graphene
import graphql_jwt
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from accounts.schema import (Query as Users,
                             Mutation as CreateUser)
from contacts.schema import (Query as Messages,
                             Mutation as AddMessage)
from posts.schema import (Query as Posts,
                          Mutation as CreatePost)
from subscription.schema import (Query as Subscribers,
                                 Mutation as AddSubscriber)


class Query(
    Users,
    Messages,
    Posts,
    Subscribers,
    graphene.ObjectType,
):
    '''Get objects from database'''
    pass


class Mutation(
    CreateUser,
    AddMessage,
    CreatePost,
    AddSubscriber,
    graphene.ObjectType,
):
    '''Add objects to database'''
    auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify = graphql_jwt.relay.Verify.Field()
    refresh = graphql_jwt.relay.Refresh.Field()
    revoke = graphql_jwt.relay.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
