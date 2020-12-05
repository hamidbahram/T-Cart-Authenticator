import graphene
import t_profile.schema




class Query(t_profile.schema.Query, graphene.ObjectType):
    pass
    


class Mutation(t_profile.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)