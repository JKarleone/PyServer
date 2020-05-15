from peewee import *
from data.Data import *
from data.Person import *
from data.Film import *


# TODO: create this table
class ScriptWriter(Data):
    id = BigAutoField()
    person = ForeignKeyField(Person)
    film = ForeignKeyField(Film)

    @staticmethod
    def add(person_id, film_id):
        error_message = ''
        try:
            ScriptWriter.create(person=person_id, film=film_id)
        except DatabaseError:
            error_message = "Can't create scriptwriter!\nWrong person id or film id"
        return error_message

    @staticmethod
    def remove_by_id(scriptwriter_id):
        error_message = ''
        try:
            ScriptWriter.get(ScriptWriter.id == scriptwriter_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete producer"
        return error_message
