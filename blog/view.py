from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin


class Blog(LoginRequiredMixin, GraphQLView):
    pass
