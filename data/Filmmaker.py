from peewee import *
from data.Data import *
from data.Person import *
from data.Film import *


# TODO: create this table
class Filmmaker(Data):
    id = BigAutoField()
    person = ForeignKeyField(Person)
    film = ForeignKeyField(Film)

    @staticmethod
    def add(person_id, film_id):
        error_message = ''
        try:
            Filmmaker.create(person=person_id, film=film_id)
        except DatabaseError:
            error_message = "Can't create new filmmaker! Wrong person or film id"
        return error_message

    @staticmethod
    def remove_by_id(filmmaker_id):
        error_message = ''
        try:
            Filmmaker.get(Filmmaker.id == filmmaker_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete filmmaker! Wrong filmmaker id"
        return error_message

    @staticmethod
    def get_name_by_film(film):
        query = Filmmaker.select().where(Filmmaker.film == film)
        return query[0].person.name
