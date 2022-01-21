from py2neo import Graph, Node, Relationship
import pandas as pd

data = pd.read_csv('data/ring_sample.csv')

# Connecting to Neo4j database
graph = Graph(password='holycross')

# Create nodes and relationships from sample data
for index, row in data.iterrows():

    person = Node('person', person_name=row['NAME'], person=row['NAME'])
    person.__primarylabel__ = 'person'
    person.__primarykey__ = 'person_name'

    address = Node('address', address_assoc=row['ADDRESS'], address=row['ADDRESS'])
    address.__primarylabel__ = 'address'
    address.__primarykey__ = 'address_assoc'

    HAS_ADDRESS = Relationship(person, 'HAS ADDRESS', address)
    graph.merge(HAS_ADDRESS)

    ssn = Node('ssn', ssn_assoc=row['SSN'], ssn=row['SSN'])
    ssn.__primarylabel__ = 'ssn'
    ssn.__primarykey__ = 'ssn_assoc'

    HAS_SSN = Relationship(person, 'HAS SSN', ssn)
    graph.merge(HAS_SSN)

    phone = Node('phone', phone_assoc=row['PHONE'], phone=row['PHONE'])
    phone.__primarylabel__ = 'phone'
    phone.__primarykey__ = 'phone_assoc'

    HAS_PHONE = Relationship(person, 'HAS PHONE', phone)
    graph.merge(HAS_PHONE)


