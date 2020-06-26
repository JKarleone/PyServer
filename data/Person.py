from peewee import *
from data.Data import *


class Person(Data):
    id = AutoField()
    name = CharField()

    @staticmethod
    def add(name):
        error_message = ''
        if Person.exists(name):
            error_message = 'This person has already been added'
            return error_message

        Person.create(name=name)
        return error_message

    @staticmethod
    def get_id_by_name(name: str):
        query = Person.select().where(Person.name == name)
        return query[0].id

    @staticmethod
    def exists(name):
        return Person.select().where(Person.name == name).exists()
