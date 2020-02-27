from flask import Flask
from flask_graphql import GraphQLView

from models import db_session, Base, engine, User, Location
from schema import schema

app = Flask(__name__)
app.debug = True

# basic stuff for db
Base.metadata.create_all(bind=engine)
loc1 = Location(country="United States", region="Nebraska", city="Omaha")
db_session.add(loc1)
loc2 = Location(country="United States", region="New York", city="New York")
db_session.add(loc1)
u1 = User(username='user1', password='pass', location=loc1)
db_session.add(u1)
u2 = User('user2', 'pass', loc2)
db_session.add(u2)
db_session.commit()

app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view(
                     'graphql', schema=schema, graphiql=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
