import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import staff_member_required
from .models import Subscriber
from blog import Connection


class SubscriberNode(DjangoObjectType):
    '''Get subscribers from database'''
    class Meta:
        model = Subscriber
        interfaces = (relay.Node, )
        connection_class = Connection
        filter_fields = {
            'email': ['icontains'],
            'name': ['icontains'],
            'terms': ['exact'],
            'status': ['exact'],
            'created': ['gt', 'lt'],
            'updated': ['gt', 'lt']
        }

    @classmethod
    @staff_member_required
    def get_node(cls, info, id):
        return Subscriber.objects.get(pk=id)


class AddSubscriber(relay.ClientIDMutation):
    '''Add subscriber to database'''
    class Input:
        email = graphene.String(required=True)
        name = graphene.String()
        terms = graphene.Boolean(required=True)
        status = graphene.Boolean()

    subscriber = graphene.Field(SubscriberNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        email = kwargs.get('email')
        name = kwargs.get('name')
        terms = kwargs.get('terms')
        status = kwargs.get('status')
        subscriber = Subscriber(email=email,
                                name=name,
                                terms=terms,
                                status=status)
        subscriber.save()
        return AddSubscriber(subscriber=subscriber)


class Query(ObjectType):
    subscriber = relay.Node.Field(SubscriberNode)
    subscribers = DjangoFilterConnectionField(SubscriberNode)

    @staff_member_required
    def resolve_subscribers(self, info, **kwargs):
        return Subscriber.objects.all()


class Mutation(ObjectType):
    add_subscriber = AddSubscriber.Field()
