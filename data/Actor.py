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

    @staticmethod
    def get_names_by_film(film):
        query = Actor.select().where(Actor.film == film)
        actors = list()
        for actor in query:
            actors.append(actor.person.name)

        return actors
