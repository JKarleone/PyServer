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
        Producer.create(person=person_id, film=film_id)

    @staticmethod
    def remove_by_id(producer_id):
        Producer.get(Producer.id == producer_id).delete_instance()
