import graphene


class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total = graphene.Int()
    count = graphene.Int()

    def resolve_total(self, info):
        return self.length

    def resolve_count(self, info):
        return len(self.edges)
