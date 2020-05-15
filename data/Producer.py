from peewee import *
from data.Data import *
from data.Person import *
from data.Film import *


# TODO: create this table
class Producer(Data):
    id = BigAutoField()
    person = ForeignKeyField(Person)
    film = ForeignKeyField(Film)

    @staticmethod
    def add(person_id, film_id):
        error_message = ''
        try:
            Producer.create(person=person_id, film=film_id)
        except DatabaseError:
            error_message = "Can't create new producer! Wrong person or film id"
        return error_message

    @staticmethod
    def remove_by_id(producer_id):
        error_message = ''
        try:
            Producer.get(Producer.id == producer_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete producer! Wrong producer id"
        return error_message
