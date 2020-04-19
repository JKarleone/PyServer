from peewee import *
from data.Data import *


class Genre(Data):
    id = AutoField()
    name = CharField()

    @staticmethod
    def add(name):
        if Genre.select().where(Genre.name == name).exists():
            print('This genre already exists')
            return

        Genre.create(name=name)

    @staticmethod
    def remove_by_id(genre_id):
        if not Genre.select().where(Genre.id == genre_id).exists():
            print('This genre doesn\'t exist')
            return

        Genre.get(Genre.id == genre_id).delete_instance()

    @staticmethod
    def get_all():
        return Genre.select()
