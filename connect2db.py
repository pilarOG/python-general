# Query databases
import pymysql
from neo4j.v1 import GraphDatabase, basic_auth

# Example of SQL query
def makeSQLquery(query, host, user, passw, db):
    try:
        connection = pymysql.connect(host=host, user=user, password=passw, db=db, cursorclass=pymysql.cursors.DictCursor, charset='utf8')
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results
    except IOError:
        raise IOError('Can\'t connect to database')

# Example to connect to Neo4j
def makeNeo4jquery(query, url, user, passw):
    try:
        driver = GraphDatabase.driver(url, auth=basic_auth(user, passw))
        session = driver.session()
        response = session.run(query)
        session.close()
        return response
    except IOError:
        raise IOError('Can\'t connect to database'')
