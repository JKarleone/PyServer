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
        error_message = ''
        if not Person.exist(person_id):
            error_message = "This person doesn't exist"
            return error_message

        if not Role.exist(role_id):
            error_message = "This role doesn't exist"
            return error_message

        if not Film.exist(film_id):
            error_message = "This film doesn't exist"
            return error_message
        Actor.create(film=film_id, person=person_id, role=role_id)
        return error_message

    @staticmethod
    def remove_by_id(actor_id):
        error_message = ''
        try:
            Actor.get(Actor.id == actor_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete actor! Wrong id"
        return error_message
