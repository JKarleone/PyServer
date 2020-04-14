from peewee import *
from data.Data import *


# TODO: create this table
class Film(Data):
    id = AutoField()
    title = CharField()
    description = TextField()
    year = SmallIntegerField()
    score = FloatField()

    @staticmethod
    def add(title, description, year, genres_id):
        if Film.select().where(Film.title == title and
                               Film.description == description and
                               Film.year == year).exists():
            print('This film has already been added')
            return

        Film.create(title=title, description=description, year=year)

        # TODO: add all genres to sub table

    @staticmethod
    def remove_by_id(film_id):
        if not Film.select().where(Film.id == film_id).exists():
            print('This film doesn\'t exist')
            return

        Film.get(Film.id == film_id).delete_instance()

        # TODO: delete connected genres with this film in sub table

    @staticmethod
    def get_all():
        return Film.select()
