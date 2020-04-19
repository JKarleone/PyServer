from peewee import *
from data.Data import *
from data.Person import *
from data.Film import *
from data.Role import *


# TODO: create this table
class Actor(Data):
    id = BigAutoField()
    film = ForeignKeyField(Film)
    person = ForeignKeyField(Person)
    role = ForeignKeyField(Role)

    @staticmethod
    def add(film_id, person_id, role_id):
        if not Person.exist(person_id):
            print('This person doesn\'t exist')
            return

        if not Role.exist(role_id):
            print('This role doesn\'t exist')
            return

        if not Film.exist(film_id):
            print('This film doesn\'t exist')
            return
        Actor.create(film=film_id, person=person_id, role=role_id)

    @staticmethod
    def remove_by_id(actor_id):
        Actor.get(Actor.id == actor_id).delete_instance()
