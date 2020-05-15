from peewee import *
from data.Data import *


# TODO: create this table #2
class Person(Data):
    id = AutoField()
    name = CharField()
    birthday = DateField()

    @staticmethod
    def add(name, birthday):
        error_message = ''
        if Person.exists(name, birthday):
            error_message = 'This person has already been added'
            return error_message

        Person.create(name=name, birthday=birthday)
        return error_message

    @staticmethod
    def remove_by_id(person_id):
        error_message = ''
        if not Person.exist(person_id):
            error_message = 'This person doesn\'t exist'
            return error_message

        Person.get(Person.id == person_id).delete_instance()
        return error_message

    @staticmethod
    def get_all():
        return Person.select()

    @staticmethod
    def exists(name, birthday):
        return Person.select().where(Person.name == name and
                                     Person.birthday == birthday).exists()
