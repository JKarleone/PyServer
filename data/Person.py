from peewee import *
from data.Data import *


# TODO: create this table #2
class Person(Data):
    id = AutoField()
    name = CharField()
    birthday = DateField()
    birthplace = CharField()

    @staticmethod
    def add(name, birthday, birthplace):
        if Person.select().where(Person.name == name and
                                 Person.birthday == birthday and
                                 Person.birthplace == birthplace).exists():
            print('This person has already been added')
            return

        Person.create(name=name, birthday=birthday, birthplace=birthplace)

    @staticmethod
    def remove_by_id(person_id):
        if not Person.exist(person_id):
            print('This person doesn\'t exist')
            return

        Person.get(Person.id == person_id).delete_instance()

    @staticmethod
    def get_all():
        return Person.select()

    @staticmethod
    def exist(person_id):
        return Person.select().where(Person.id == person_id).exists()
