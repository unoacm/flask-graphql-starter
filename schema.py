import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, User as UserModel, Location as LocationModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    """
    This serves as the entrypoint into the "graph" of objects to query
    """

    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User)
    all_departments = SQLAlchemyConnectionField(Location)


schema = graphene.Schema(query=Query)
