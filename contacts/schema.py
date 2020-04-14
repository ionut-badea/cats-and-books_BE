import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import staff_member_required
from .models import Message
from blog import Connection


class MessageNode(DjangoObjectType):
    '''Get messages from database'''
    class Meta:
        model = Message
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'email': ['icontains'],
            'name': ['icontains'],
            'body': ['icontains'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt'],
            'reply': ['exact']
        }

    @classmethod
    @staff_member_required
    def get_node(cls, info, id):
        return Message.objects.get(pk=id)


class AddMessage(relay.ClientIDMutation):
    '''Add message to database'''
    class Input:
        email = graphene.String(required=True)
        name = graphene.String()
        body = graphene.String(required=True)
        terms = graphene.Boolean(required=True)

    message = graphene.Field(MessageNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        email = kwargs.get('email')
        name = kwargs.get('name')
        body = kwargs.get('body')
        terms = kwargs.get('terms')
        message = Message(email=email,
                          name=name,
                          body=body,
                          terms=terms)
        message.save()
        return AddMessage(message=message)


class Query(ObjectType):
    message = relay.Node.Field(MessageNode)
    messages = DjangoFilterConnectionField(MessageNode)

    @staff_member_required
    def resolve_messages(self, info, **kwargs):
        return Message.objects.all()


class Mutation(ObjectType):
    add_message = AddMessage.Field()
