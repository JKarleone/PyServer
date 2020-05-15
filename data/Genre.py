from peewee import *
from data.Data import *


class Genre(Data):
    id = AutoField()
    name = CharField()

    @staticmethod
    def add(name):
        error_message = ''
        if Genre.select().where(Genre.name == name).exists():
            error_message = 'This genre already exists'
            return error_message

        Genre.create(name=name)
        return error_message

    @staticmethod
    def remove_by_id(genre_id):
        error_message = ''
        if not Genre.exists(genre_id):
            error_message = "This genre doesn't exist"
            return error_message

        Genre.get(Genre.id == genre_id).delete_instance()
        return error_message

    @staticmethod
    def exists(genre_id):
        return Genre.select().where(Genre.id == genre_id)

    @staticmethod
    def get_all():
        return Genre.select()
