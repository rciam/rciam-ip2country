#!/usr/bin/python
from configparser import ConfigParser

import psycopg2

def singleton(theClass):
    """ decorator for a class to make a singleton out of it """
    classInstances = {}

    def getInstance(*args, **kwargs):
        """ creating or just return the one and only class instance.
            The singleton depends on the parameters used in __init__ """
        key = (theClass, args, str(kwargs))
        if key not in classInstances:
            classInstances[key] = theClass(*args, **kwargs)
        return classInstances[key]

    return getInstance

@singleton
class pgConnector:
  
  conn = None
  #__instance = None
  #@staticmethod 
  #def getInstance():
  #    """ Static access method. """
  #    if pgConnector.__instance == None:
  #       pgConnector()
  #    return pgConnector.__instance

  def __init__(self, filename = "database.ini", section = "postgresql"):

    self.filename = filename
    self.section = section
    self.params = self.config(filename, section)
    if self.conn == None:
      self.conn = psycopg2.connect(**self.params)
    print (self.params)

  def config(self, filename='database.ini', section='postgresql'):

    # create a parser

    parser = ConfigParser()

    # read config file

    parser.read(filename)



    # get section, default to postgresql

    db = {}

    if parser.has_section(section):

        params = parser.items(section)

        for param in params:

            db[param[0]] = param[1]

    else:

        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


  def connect(self):

    # connect to the PostgreSQL server

    print('Connecting to the PostgreSQL database...')

    self.conn = psycopg2.connect(**self.params)

  def execute_select(self, query):

    # create a cursor

    cur = self.conn.cursor()

    # execute a statement

    #print('PostgreSQL database version:')

    cur.execute(query)

    return cur.fetchall()

  def execute_insert(self, query):
    cur = self.conn.cursor()
    cur.execute(query)
    #id = cur.fetchone()[0]
    self.conn.commit()


  def close(self):

    self.conn.close()

    print('Database connection closed.')

""" p1 = pgConnector("database.ini","postgresql")
print(p1)
#p1.connect()
p1.execute("SELECT version()")
p1.close()
p2 = pgConnector("database.ini","postgresql")
print(p2) """

