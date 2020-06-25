from peewee import *
from data.Data import *
from data.Person import *
from data.Film import *


class Actor(Data):
    id = BigAutoField()
    film = ForeignKeyField(Film)
    person = ForeignKeyField(Person)

    @staticmethod
    def add(film_id, person_id):
        error_message = ''
        if not Person.exist(person_id):
            error_message = "This person doesn't exist"
            return error_message

        if not Film.exist(film_id):
            error_message = "This film doesn't exist"
            return error_message
        Actor.create(film=film_id, person=person_id)
        return error_message

    @staticmethod
    def remove_by_id(actor_id):
        error_message = ''
        try:
            Actor.get(Actor.id == actor_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete actor! Wrong id"
        return error_message
