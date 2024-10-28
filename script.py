from pprint import pprint

from models.client import Client
from models import storage

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.common import Base  # Your base class with metadata

storage.drop_all_tables()

# Define your database URL
DATABASE_URL = os.getenv('CARTOFIX_DB_CONNECTION_STRING')
engine = create_engine(DATABASE_URL)

# Create the table explicitly
Client.__table__.create(engine)

client = Client(name="Julien", mail="mail@gmail.com", phone_number="1021328120")
client.save()
pprint(storage.get(Client, client.oid).__dict__)

