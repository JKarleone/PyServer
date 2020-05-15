from peewee import *
from data.Data import *
from data.Film import *


# TODO: create this table
class Role(Data):
    id = AutoField()
    role_name = CharField()
    film = ForeignKeyField(Film)

    @staticmethod
    def add(role_name, film_id):
        Role.create(role_name=role_name, film=film_id)

    @staticmethod
    def remove_by_id(role_id):
        error_message = ''
        if not Role.exist(role_id):
            error_message = 'This role doesn\'t exist'
            return error_message

        Role.get(Role.id == role_id).delete_instance()
        return error_message

    @staticmethod
    def exist(role_id):
        return Role.select().where(Role.id == role_id).exists()
