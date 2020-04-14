from peewee import *


class Data(Model):
    class Meta:
        database = PostgresqlDatabase(database='Project',
                                      user='postgres',
                                      password='admin',
                                      host='localhost',
                                      port=5432)